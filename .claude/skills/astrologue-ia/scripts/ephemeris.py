#!/usr/bin/env python3
"""
Ephemeris Calculator - Swiss Ephemeris based astrological calculations.

Provides reliable natal chart, transit, and aspect calculations
using pyswisseph (Swiss Ephemeris) without external API dependencies.

Usage:
    python3 ephemeris.py natal --date 14.11.1994 --time 13:04 --lat 43.71 --lon 7.26
    python3 ephemeris.py transits --date 14.11.1994 --time 13:04 --lat 43.71 --lon 7.26 --year 2026
    python3 ephemeris.py ephemeris --year 2026 --month 2
    python3 ephemeris.py solar-return --date 14.11.1994 --time 13:04 --lat 43.71 --lon 7.26 --year 2026
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Optional

try:
    import swisseph as swe
except ImportError:
    print("ERROR: pyswisseph not installed. Run: pip install pyswisseph", file=sys.stderr)
    sys.exit(1)

# Use Moshier ephemeris (built-in, no external files needed)
swe.set_ephe_path("")

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
    "North Node": swe.MEAN_NODE,
}

ASPECT_TYPES = {
    "conjunction": {"angle": 0, "orb": 8, "symbol": "☌"},
    "opposition": {"angle": 180, "orb": 8, "symbol": "☍"},
    "square": {"angle": 90, "orb": 7, "symbol": "□"},
    "trine": {"angle": 120, "orb": 8, "symbol": "△"},
    "sextile": {"angle": 60, "orb": 6, "symbol": "⚹"},
    "quincunx": {"angle": 150, "orb": 3, "symbol": "⚻"},
}


def get_sign(longitude: float) -> dict:
    """Convert ecliptic longitude to sign, degree, minute."""
    sign_idx = int(longitude / 30)
    degree_in_sign = longitude % 30
    degrees = int(degree_in_sign)
    minutes = int((degree_in_sign - degrees) * 60)
    return {
        "sign": SIGNS[sign_idx],
        "sign_index": sign_idx,
        "degree": degrees,
        "minute": minutes,
        "longitude": round(longitude, 4),
        "formatted": f"{SIGNS[sign_idx]} {degrees}°{minutes:02d}'",
    }


def calc_planet(jd: float, planet_id: int) -> dict:
    """Calculate a planet's position for a given Julian Day."""
    try:
        result = swe.calc_ut(jd, planet_id)
        lon = result[0][0]
        lat = result[0][1]
        speed = result[0][3]
        is_retrograde = speed < 0
        sign_info = get_sign(lon)
        return {
            **sign_info,
            "latitude": round(lat, 4),
            "speed": round(speed, 4),
            "retrograde": is_retrograde,
        }
    except swe.Error:
        return None


def calc_houses(jd: float, lat: float, lon: float, system: str = "P") -> dict:
    """Calculate house cusps and angles. Default: Placidus."""
    houses_data = swe.houses(jd, lat, lon, system.encode())
    cusps = houses_data[0]  # 12 house cusps
    angles = houses_data[1]  # ASC, MC, ARMC, Vertex, etc.

    asc = angles[0]
    mc = angles[1]
    dsc = (asc + 180) % 360
    ic = (mc + 180) % 360

    house_cusps = {}
    for i in range(12):
        house_cusps[f"H{i+1}"] = get_sign(cusps[i])

    return {
        "cusps": house_cusps,
        "ASC": get_sign(asc),
        "MC": get_sign(mc),
        "DSC": get_sign(dsc),
        "IC": get_sign(ic),
    }


def get_house_for_planet(planet_lon: float, cusps: list) -> int:
    """Determine which house a planet falls in based on house cusps."""
    for i in range(12):
        cusp_start = cusps[i]
        cusp_end = cusps[(i + 1) % 12]
        if cusp_start < cusp_end:
            if cusp_start <= planet_lon < cusp_end:
                return i + 1
        else:  # Wraps around 0° Aries
            if planet_lon >= cusp_start or planet_lon < cusp_end:
                return i + 1
    return 1


def calc_aspect(lon1: float, lon2: float) -> Optional[dict]:
    """Check if two longitudes form a major aspect."""
    diff = abs(lon1 - lon2)
    if diff > 180:
        diff = 360 - diff

    for name, info in ASPECT_TYPES.items():
        orb = abs(diff - info["angle"])
        if orb <= info["orb"]:
            return {
                "type": name,
                "angle": info["angle"],
                "symbol": info["symbol"],
                "orb": round(orb, 2),
                "applying": None,  # Would need speed comparison
            }
    return None


def parse_date(date_str: str) -> tuple:
    """Parse date in DD.MM.YYYY format."""
    parts = date_str.split(".")
    return int(parts[2]), int(parts[1]), int(parts[0])


def parse_time(time_str: str) -> float:
    """Parse time in HH:MM format, return decimal hours."""
    parts = time_str.split(":")
    return int(parts[0]) + int(parts[1]) / 60.0


def local_to_ut(decimal_hours: float, date_tuple: tuple, timezone_offset: float = 1.0) -> float:
    """Convert local time to Universal Time. Default offset=1 for CET."""
    return decimal_hours - timezone_offset


def natal_chart(date_str: str, time_str: str, lat: float, lon: float,
                tz_offset: float = 1.0) -> dict:
    """Calculate a complete natal chart."""
    year, month, day = parse_date(date_str)
    local_hours = parse_time(time_str)
    ut_hours = local_to_ut(local_hours, (year, month, day), tz_offset)

    jd = swe.julday(year, month, day, ut_hours)

    # Calculate planets
    planets = {}
    for name, pid in PLANETS.items():
        pos = calc_planet(jd, pid)
        if pos:
            planets[name] = pos

    # Calculate houses
    houses = calc_houses(jd, lat, lon)

    # Assign houses to planets
    cusps_list = [houses["cusps"][f"H{i+1}"]["longitude"] for i in range(12)]
    for name in planets:
        planets[name]["house"] = get_house_for_planet(planets[name]["longitude"], cusps_list)

    # Calculate aspects between all planet pairs
    aspects = []
    planet_names = list(planets.keys())
    for i in range(len(planet_names)):
        for j in range(i + 1, len(planet_names)):
            p1, p2 = planet_names[i], planet_names[j]
            aspect = calc_aspect(planets[p1]["longitude"], planets[p2]["longitude"])
            if aspect:
                aspects.append({
                    "planet1": p1,
                    "planet2": p2,
                    **aspect,
                })

    return {
        "birth_data": {
            "date": date_str,
            "time": time_str,
            "latitude": lat,
            "longitude": lon,
            "timezone_offset": tz_offset,
            "julian_day": jd,
        },
        "planets": planets,
        "houses": houses,
        "aspects": aspects,
    }


def find_retrogrades(year: int, planet_id: int, planet_name: str) -> list:
    """Find retrograde periods for a planet during a given year."""
    retrogrades = []
    jd_start = swe.julday(year, 1, 1, 0.0)
    jd_end = swe.julday(year, 12, 31, 23.99)

    in_retro = False
    retro_start = None
    step = 1.0  # Daily steps

    jd = jd_start
    while jd <= jd_end:
        pos = swe.calc_ut(jd, planet_id)
        speed = pos[0][3]
        is_retro = speed < 0

        if is_retro and not in_retro:
            retro_start = jd
            in_retro = True
        elif not is_retro and in_retro:
            # Retrograde ended
            start_date = swe.revjul(retro_start)
            end_date = swe.revjul(jd)
            start_sign = get_sign(swe.calc_ut(retro_start, planet_id)[0][0])
            end_sign = get_sign(swe.calc_ut(jd, planet_id)[0][0])
            retrogrades.append({
                "planet": planet_name,
                "start": f"{int(start_date[2]):02d}.{int(start_date[1]):02d}.{int(start_date[0])}",
                "end": f"{int(end_date[2]):02d}.{int(end_date[1]):02d}.{int(end_date[0])}",
                "start_sign": start_sign["formatted"],
                "end_sign": end_sign["formatted"],
            })
            in_retro = False

        jd += step

    # If still retrograde at year end
    if in_retro and retro_start:
        start_date = swe.revjul(retro_start)
        start_sign = get_sign(swe.calc_ut(retro_start, planet_id)[0][0])
        retrogrades.append({
            "planet": planet_name,
            "start": f"{int(start_date[2]):02d}.{int(start_date[1]):02d}.{int(start_date[0])}",
            "end": f"ongoing into {year + 1}",
            "start_sign": start_sign["formatted"],
            "end_sign": "ongoing",
        })

    return retrogrades


def find_sign_ingresses(year: int, planet_id: int, planet_name: str) -> list:
    """Find when a planet changes signs during a year."""
    ingresses = []
    jd_start = swe.julday(year, 1, 1, 0.0)
    jd_end = swe.julday(year, 12, 31, 23.99)

    prev_sign = None
    step = 1.0
    if planet_id in (swe.MOON,):
        step = 0.25  # Moon moves fast
    elif planet_id in (swe.SUN, swe.MERCURY, swe.VENUS, swe.MARS):
        step = 0.5

    jd = jd_start
    while jd <= jd_end:
        pos = swe.calc_ut(jd, planet_id)
        current_sign = int(pos[0][0] / 30)

        if prev_sign is not None and current_sign != prev_sign:
            date = swe.revjul(jd)
            ingresses.append({
                "planet": planet_name,
                "date": f"{int(date[2]):02d}.{int(date[1]):02d}.{int(date[0])}",
                "from_sign": SIGNS[prev_sign],
                "to_sign": SIGNS[current_sign],
            })

        prev_sign = current_sign
        jd += step

    return ingresses


def find_new_full_moons(year: int) -> list:
    """Find all New Moons and Full Moons in a year."""
    events = []
    jd_start = swe.julday(year, 1, 1, 0.0)
    jd_end = swe.julday(year, 12, 31, 23.99)

    step = 0.5  # Check twice per day
    prev_diff = None

    jd = jd_start
    while jd <= jd_end:
        sun = swe.calc_ut(jd, swe.SUN)[0][0]
        moon = swe.calc_ut(jd, swe.MOON)[0][0]
        diff = (moon - sun) % 360

        if prev_diff is not None:
            # New Moon: diff crosses 0 (from ~350+ to ~0+)
            if prev_diff > 340 and diff < 20:
                date = swe.revjul(jd)
                moon_sign = get_sign(moon)
                events.append({
                    "type": "New Moon",
                    "date": f"{int(date[2]):02d}.{int(date[1]):02d}.{int(date[0])}",
                    "sign": moon_sign["formatted"],
                    "longitude": moon_sign["longitude"],
                })
            # Full Moon: diff crosses 180
            elif prev_diff < 180 and diff >= 180:
                date = swe.revjul(jd)
                moon_sign = get_sign(moon)
                events.append({
                    "type": "Full Moon",
                    "date": f"{int(date[2]):02d}.{int(date[1]):02d}.{int(date[0])}",
                    "sign": moon_sign["formatted"],
                    "longitude": moon_sign["longitude"],
                })

        prev_diff = diff
        jd += step

    return events


def find_eclipses(year: int) -> list:
    """Find solar and lunar eclipses for a given year."""
    eclipses = []

    # Search for solar eclipses
    jd_start = swe.julday(year, 1, 1, 0.0)
    jd = jd_start

    for _ in range(3):  # Max 3 solar eclipses per year
        try:
            result = swe.sol_eclipse_when_glob(jd, swe.FLG_SWIEPH)
            eclipse_jd = result[1][0]
            date = swe.revjul(eclipse_jd)
            if int(date[0]) == year:
                sun_pos = get_sign(swe.calc_ut(eclipse_jd, swe.SUN)[0][0])
                eclipse_type = "Total" if result[0] & swe.ECL_TOTAL else \
                               "Annular" if result[0] & swe.ECL_ANNULAR else "Partial"
                eclipses.append({
                    "type": f"Solar Eclipse ({eclipse_type})",
                    "date": f"{int(date[2]):02d}.{int(date[1]):02d}.{int(date[0])}",
                    "sign": sun_pos["formatted"],
                    "longitude": sun_pos["longitude"],
                })
                jd = eclipse_jd + 30
            else:
                break
        except Exception:
            break

    # Search for lunar eclipses
    jd = jd_start
    for _ in range(3):
        try:
            result = swe.lun_eclipse_when(jd, swe.FLG_SWIEPH)
            eclipse_jd = result[1][0]
            date = swe.revjul(eclipse_jd)
            if int(date[0]) == year:
                moon_pos = get_sign(swe.calc_ut(eclipse_jd, swe.MOON)[0][0])
                eclipse_type = "Total" if result[0] & swe.ECL_TOTAL else \
                               "Partial" if result[0] & swe.ECL_PARTIAL else "Penumbral"
                eclipses.append({
                    "type": f"Lunar Eclipse ({eclipse_type})",
                    "date": f"{int(date[2]):02d}.{int(date[1]):02d}.{int(date[0])}",
                    "sign": moon_pos["formatted"],
                    "longitude": moon_pos["longitude"],
                })
                jd = eclipse_jd + 30
            else:
                break
        except Exception:
            break

    eclipses.sort(key=lambda x: x["date"])
    return eclipses


def calc_transits_to_natal(natal: dict, year: int) -> list:
    """Calculate major transits to natal chart positions for a given year."""
    transits = []
    slow_planets = {
        "Jupiter": swe.JUPITER,
        "Saturn": swe.SATURN,
        "Uranus": swe.URANUS,
        "Neptune": swe.NEPTUNE,
        "Pluto": swe.PLUTO,
    }

    natal_points = {}
    for name, data in natal["planets"].items():
        natal_points[name] = data["longitude"]
    natal_points["ASC"] = natal["houses"]["ASC"]["longitude"]
    natal_points["MC"] = natal["houses"]["MC"]["longitude"]
    natal_points["DSC"] = natal["houses"]["DSC"]["longitude"]
    natal_points["IC"] = natal["houses"]["IC"]["longitude"]

    jd_start = swe.julday(year, 1, 1, 0.0)

    for transit_name, transit_id in slow_planets.items():
        # Sample monthly positions
        for month in range(1, 13):
            jd = swe.julday(year, month, 15, 12.0)
            transit_pos = swe.calc_ut(jd, transit_id)
            transit_lon = transit_pos[0][0]

            for natal_name, natal_lon in natal_points.items():
                aspect = calc_aspect(transit_lon, natal_lon)
                if aspect and aspect["type"] in ("conjunction", "opposition", "square", "trine"):
                    date = swe.revjul(jd)
                    transits.append({
                        "transit_planet": transit_name,
                        "natal_point": natal_name,
                        "aspect": aspect["type"],
                        "symbol": aspect["symbol"],
                        "orb": aspect["orb"],
                        "month": f"{int(date[1]):02d}/{int(date[0])}",
                        "transit_position": get_sign(transit_lon)["formatted"],
                        "natal_position": get_sign(natal_lon)["formatted"],
                    })

    # Deduplicate (same transit may appear in consecutive months)
    seen = set()
    unique_transits = []
    for t in transits:
        key = f"{t['transit_planet']}-{t['natal_point']}-{t['aspect']}"
        if key not in seen:
            seen.add(key)
            unique_transits.append(t)

    return sorted(unique_transits, key=lambda x: x["month"])


def find_major_conjunctions(year: int) -> list:
    """Find major outer planet conjunctions during the year."""
    conjunctions = []
    pairs = [
        ("Saturn", swe.SATURN, "Neptune", swe.NEPTUNE, 36),
        ("Jupiter", swe.JUPITER, "Saturn", swe.SATURN, 20),
        ("Jupiter", swe.JUPITER, "Uranus", swe.URANUS, 14),
        ("Jupiter", swe.JUPITER, "Neptune", swe.NEPTUNE, 13),
        ("Jupiter", swe.JUPITER, "Pluto", swe.PLUTO, 13),
    ]

    for name1, id1, name2, id2, cycle_years in pairs:
        closest_jd = None
        min_diff = 999

        for month in range(1, 13):
            for day in (1, 15):
                jd = swe.julday(year, month, day, 12.0)
                pos1 = swe.calc_ut(jd, id1)[0][0]
                pos2 = swe.calc_ut(jd, id2)[0][0]
                diff = abs(pos1 - pos2)
                if diff > 180:
                    diff = 360 - diff
                if diff < min_diff:
                    min_diff = diff
                    closest_jd = jd

        if min_diff < 5.0:  # Within 5 degrees = notable
            date = swe.revjul(closest_jd)
            pos1 = get_sign(swe.calc_ut(closest_jd, id1)[0][0])
            pos2 = get_sign(swe.calc_ut(closest_jd, id2)[0][0])
            conjunctions.append({
                "planets": f"{name1}-{name2}",
                "date": f"{int(date[2]):02d}.{int(date[1]):02d}.{int(date[0])}",
                "separation": round(min_diff, 2),
                "exact": min_diff < 1.0,
                "position": pos1["formatted"],
                "cycle": f"Every ~{cycle_years} years",
            })

    return conjunctions


def monthly_ephemeris(year: int, month: int) -> dict:
    """Generate daily ephemeris for a given month."""
    import calendar
    days_in_month = calendar.monthrange(year, month)[1]

    daily = []
    for day in range(1, days_in_month + 1):
        jd = swe.julday(year, month, day, 12.0)
        day_data = {"date": f"{day:02d}.{month:02d}.{year}"}
        for name, pid in PLANETS.items():
            pos = calc_planet(jd, pid)
            if pos:
                day_data[name] = {
                    "position": pos["formatted"],
                    "retrograde": pos["retrograde"],
                }
        daily.append(day_data)

    return {"year": year, "month": month, "daily": daily}


def solar_return(natal_date: str, natal_time: str, lat: float, lon: float,
                 sr_year: int, tz_offset: float = 1.0) -> dict:
    """Calculate Solar Return chart for a given year."""
    year, month, day = parse_date(natal_date)
    local_hours = parse_time(natal_time)
    ut_hours = local_to_ut(local_hours, (year, month, day), tz_offset)

    jd_natal = swe.julday(year, month, day, ut_hours)
    natal_sun = swe.calc_ut(jd_natal, swe.SUN)[0][0]

    # Search for exact Solar Return in the target year
    jd_search = swe.julday(sr_year, month, day - 2, 0.0)
    jd_end = swe.julday(sr_year, month, day + 2, 23.99)

    step = 0.01  # ~15 minute precision
    best_jd = jd_search
    min_diff = 999

    jd = jd_search
    while jd <= jd_end:
        sun_pos = swe.calc_ut(jd, swe.SUN)[0][0]
        diff = abs(sun_pos - natal_sun)
        if diff > 180:
            diff = 360 - diff
        if diff < min_diff:
            min_diff = diff
            best_jd = jd
        jd += step

    # Now get the full chart for that moment
    sr_date = swe.revjul(best_jd)

    planets = {}
    for name, pid in PLANETS.items():
        pos = calc_planet(best_jd, pid)
        if pos:
            planets[name] = pos

    houses = calc_houses(best_jd, lat, lon)

    cusps_list = [houses["cusps"][f"H{i+1}"]["longitude"] for i in range(12)]
    for name in planets:
        planets[name]["house"] = get_house_for_planet(planets[name]["longitude"], cusps_list)

    return {
        "type": "Solar Return",
        "year": sr_year,
        "exact_date": f"{int(sr_date[2]):02d}.{int(sr_date[1]):02d}.{int(sr_date[0])}",
        "exact_time_ut": f"{int(sr_date[3]):02d}:{int((sr_date[3] % 1) * 60):02d} UT",
        "location": {"latitude": lat, "longitude": lon},
        "planets": planets,
        "houses": houses,
    }


def composite_chart(chart1: dict, chart2: dict, lat: float, lon: float) -> dict:
    """Calculate composite chart (midpoint method) from two natal charts."""
    comp_planets = {}
    for name in chart1["planets"]:
        if name in chart2["planets"]:
            lon1 = chart1["planets"][name]["longitude"]
            lon2 = chart2["planets"][name]["longitude"]
            # Calculate midpoint (shortest arc)
            diff = lon2 - lon1
            if diff > 180:
                diff -= 360
            elif diff < -180:
                diff += 360
            midpoint = (lon1 + diff / 2) % 360
            comp_planets[name] = get_sign(midpoint)
            comp_planets[name]["retrograde"] = False

    # Composite ASC/MC midpoints
    asc1 = chart1["houses"]["ASC"]["longitude"]
    asc2 = chart2["houses"]["ASC"]["longitude"]
    mc1 = chart1["houses"]["MC"]["longitude"]
    mc2 = chart2["houses"]["MC"]["longitude"]

    diff_asc = asc2 - asc1
    if diff_asc > 180: diff_asc -= 360
    elif diff_asc < -180: diff_asc += 360
    comp_asc = (asc1 + diff_asc / 2) % 360

    diff_mc = mc2 - mc1
    if diff_mc > 180: diff_mc -= 360
    elif diff_mc < -180: diff_mc += 360
    comp_mc = (mc1 + diff_mc / 2) % 360

    # Calculate aspects
    aspects = []
    planet_names = list(comp_planets.keys())
    for i in range(len(planet_names)):
        for j in range(i + 1, len(planet_names)):
            p1, p2 = planet_names[i], planet_names[j]
            aspect = calc_aspect(comp_planets[p1]["longitude"], comp_planets[p2]["longitude"])
            if aspect:
                aspects.append({"planet1": p1, "planet2": p2, **aspect})

    return {
        "type": "Composite",
        "planets": comp_planets,
        "ASC": get_sign(comp_asc),
        "MC": get_sign(comp_mc),
        "DSC": get_sign((comp_asc + 180) % 360),
        "IC": get_sign((comp_mc + 180) % 360),
        "aspects": aspects,
    }


def davison_chart(date1: str, time1: str, lat1: float, lon1: float,
                  date2: str, time2: str, lat2: float, lon2: float,
                  tz1: float = 1.0, tz2: float = 1.0) -> dict:
    """Calculate Davison relationship chart (midpoint in time and space)."""
    y1, m1, d1 = parse_date(date1)
    y2, m2, d2 = parse_date(date2)
    h1 = local_to_ut(parse_time(time1), (y1, m1, d1), tz1)
    h2 = local_to_ut(parse_time(time2), (y2, m2, d2), tz2)

    jd1 = swe.julday(y1, m1, d1, h1)
    jd2 = swe.julday(y2, m2, d2, h2)
    jd_mid = (jd1 + jd2) / 2
    lat_mid = (lat1 + lat2) / 2
    lon_mid = (lon1 + lon2) / 2

    mid_date = swe.revjul(jd_mid)

    planets = {}
    for name, pid in PLANETS.items():
        pos = calc_planet(jd_mid, pid)
        if pos:
            planets[name] = pos

    houses = calc_houses(jd_mid, lat_mid, lon_mid)
    cusps_list = [houses["cusps"][f"H{i+1}"]["longitude"] for i in range(12)]
    for name in planets:
        planets[name]["house"] = get_house_for_planet(planets[name]["longitude"], cusps_list)

    return {
        "type": "Davison",
        "midpoint_date": f"{int(mid_date[2]):02d}.{int(mid_date[1]):02d}.{int(mid_date[0])}",
        "midpoint_time_ut": f"{int(mid_date[3]):02d}:{int((mid_date[3] % 1) * 60):02d} UT",
        "midpoint_location": {"latitude": round(lat_mid, 2), "longitude": round(lon_mid, 2)},
        "planets": planets,
        "houses": houses,
    }


def progressed_chart(natal_date: str, natal_time: str, lat: float, lon: float,
                     target_age: int, tz_offset: float = 1.0) -> dict:
    """Calculate secondary progressions (1 day = 1 year)."""
    year, month, day = parse_date(natal_date)
    local_hours = parse_time(natal_time)
    ut_hours = local_to_ut(local_hours, (year, month, day), tz_offset)

    jd_natal = swe.julday(year, month, day, ut_hours)
    jd_progressed = jd_natal + target_age  # 1 day per year

    prog_date = swe.revjul(jd_progressed)

    planets = {}
    for name, pid in PLANETS.items():
        pos = calc_planet(jd_progressed, pid)
        if pos:
            planets[name] = pos

    # Compare with natal for direction changes
    natal_planets = {}
    for name, pid in PLANETS.items():
        pos = calc_planet(jd_natal, pid)
        if pos:
            natal_planets[name] = pos

    direction_changes = []
    for name in planets:
        if name in natal_planets:
            if planets[name]["retrograde"] != natal_planets[name]["retrograde"]:
                change = "direct → retrograde" if planets[name]["retrograde"] else "retrograde → direct"
                direction_changes.append({"planet": name, "change": change})

    houses = calc_houses(jd_progressed, lat, lon)
    cusps_list = [houses["cusps"][f"H{i+1}"]["longitude"] for i in range(12)]
    for name in planets:
        planets[name]["house"] = get_house_for_planet(planets[name]["longitude"], cusps_list)

    # Calculate aspects between progressed and natal
    prog_to_natal = []
    for pname, pdata in planets.items():
        for nname, ndata in natal_planets.items():
            aspect = calc_aspect(pdata["longitude"], ndata["longitude"])
            if aspect and aspect["type"] in ("conjunction", "opposition", "square", "trine"):
                prog_to_natal.append({
                    "progressed": pname,
                    "natal": nname,
                    **aspect,
                })

    return {
        "type": "Secondary Progressions",
        "age": target_age,
        "progressed_date": f"{int(prog_date[2]):02d}.{int(prog_date[1]):02d}.{int(prog_date[0])}",
        "planets": planets,
        "natal_planets": natal_planets,
        "houses": houses,
        "direction_changes": direction_changes,
        "progressed_to_natal_aspects": prog_to_natal,
    }


def profection(natal_date: str, natal_time: str, lat: float, lon: float,
               target_age: int, tz_offset: float = 1.0) -> dict:
    """Calculate annual profection for a given age."""
    chart = natal_chart(natal_date, natal_time, lat, lon, tz_offset)

    profection_house = (target_age % 12) + 1
    cusp_sign = chart["houses"]["cusps"][f"H{profection_house}"]

    # Determine Time Lord (traditional ruler of the profection sign)
    traditional_rulers = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
        "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
        "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
        "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter",
    }
    time_lord_name = traditional_rulers.get(cusp_sign["sign"], "Unknown")
    time_lord_data = chart["planets"].get(time_lord_name)

    house_themes = {
        1: "Identité, corps, nouveau cycle",
        2: "Argent, valeurs, possessions",
        3: "Communication, fratrie, apprentissage",
        4: "Famille, foyer, racines",
        5: "Créativité, romance, enfants",
        6: "Santé, travail quotidien, routine",
        7: "Relations, mariage, partenariats",
        8: "Transformation, sexe, crises, héritage",
        9: "Voyages, spiritualité, études",
        10: "Carrière, réputation, ambition",
        11: "Amis, espoirs, communauté",
        12: "Solitude, spiritualité, auto-sabotage",
    }

    return {
        "type": "Annual Profection",
        "age": target_age,
        "profection_house": profection_house,
        "profection_sign": cusp_sign["sign"],
        "theme": house_themes.get(profection_house, ""),
        "time_lord": {
            "name": time_lord_name,
            "natal_position": time_lord_data["formatted"] if time_lord_data else "N/A",
            "natal_house": time_lord_data.get("house", "N/A") if time_lord_data else "N/A",
            "retrograde": time_lord_data["retrograde"] if time_lord_data else False,
        },
    }


def draconic_chart(natal_date: str, natal_time: str, lat: float, lon: float,
                   tz_offset: float = 1.0) -> dict:
    """Calculate draconic chart (North Node = 0° Aries)."""
    chart = natal_chart(natal_date, natal_time, lat, lon, tz_offset)
    nn_lon = chart["planets"]["North Node"]["longitude"]

    draconic_planets = {}
    for name, data in chart["planets"].items():
        drac_lon = (data["longitude"] - nn_lon) % 360
        drac_info = get_sign(drac_lon)
        draconic_planets[name] = {
            **drac_info,
            "natal_position": data["formatted"],
            "retrograde": data["retrograde"],
        }

    # Draconic angles
    drac_asc = (chart["houses"]["ASC"]["longitude"] - nn_lon) % 360
    drac_mc = (chart["houses"]["MC"]["longitude"] - nn_lon) % 360

    return {
        "type": "Draconic",
        "nn_offset": round(nn_lon, 4),
        "planets": draconic_planets,
        "ASC": get_sign(drac_asc),
        "MC": get_sign(drac_mc),
        "DSC": get_sign((drac_asc + 180) % 360),
        "IC": get_sign((drac_mc + 180) % 360),
    }


def format_natal_text(chart: dict) -> str:
    """Format natal chart as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append(f"  NATAL CHART - {chart['birth_data']['date']} {chart['birth_data']['time']}")
    lines.append(f"  Lat: {chart['birth_data']['latitude']} Lon: {chart['birth_data']['longitude']}")
    lines.append("=" * 60)
    lines.append("")

    lines.append("--- PLANETS ---")
    for name, data in chart["planets"].items():
        retro = " (R)" if data["retrograde"] else ""
        house = f"  [H{data['house']}]" if "house" in data else ""
        lines.append(f"  {name:12s} {data['formatted']}{retro}{house}")

    lines.append("")
    lines.append("--- ANGLES ---")
    for angle in ("ASC", "MC", "DSC", "IC"):
        lines.append(f"  {angle:12s} {chart['houses'][angle]['formatted']}")

    lines.append("")
    lines.append("--- HOUSE CUSPS ---")
    for i in range(1, 13):
        cusp = chart["houses"]["cusps"][f"H{i}"]
        lines.append(f"  H{i:2d}          {cusp['formatted']}")

    lines.append("")
    lines.append("--- ASPECTS ---")
    for asp in chart["aspects"]:
        lines.append(
            f"  {asp['planet1']:12s} {asp['symbol']} {asp['planet2']:12s} "
            f"({asp['type']}, orb {asp['orb']}°)"
        )

    return "\n".join(lines)


def format_transits_text(natal: dict, year: int) -> str:
    """Format transit analysis as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append(f"  TRANSITS {year} for natal chart {natal['birth_data']['date']}")
    lines.append("=" * 60)

    # Major conjunctions
    conjs = find_major_conjunctions(year)
    if conjs:
        lines.append("")
        lines.append("--- MAJOR CONJUNCTIONS ---")
        for c in conjs:
            exact = " **EXACT**" if c["exact"] else ""
            lines.append(f"  {c['planets']:20s} {c['date']} at {c['position']} (sep: {c['separation']}°){exact}")
            lines.append(f"  {'':20s} Cycle: {c['cycle']}")

    # Eclipses
    eclipses = find_eclipses(year)
    if eclipses:
        lines.append("")
        lines.append("--- ECLIPSES ---")
        for e in eclipses:
            lines.append(f"  {e['date']}  {e['type']:30s} at {e['sign']}")

    # Retrogrades
    lines.append("")
    lines.append("--- RETROGRADES ---")
    for name, pid in [("Mercury", swe.MERCURY), ("Venus", swe.VENUS), ("Mars", swe.MARS),
                       ("Jupiter", swe.JUPITER), ("Saturn", swe.SATURN),
                       ("Uranus", swe.URANUS), ("Neptune", swe.NEPTUNE), ("Pluto", swe.PLUTO)]:
        retros = find_retrogrades(year, pid, name)
        for r in retros:
            lines.append(f"  {r['planet']:10s} {r['start']} -> {r['end']}  ({r['start_sign']} -> {r['end_sign']})")

    # Sign ingresses (slow planets)
    lines.append("")
    lines.append("--- SIGN CHANGES (outer planets) ---")
    for name, pid in [("Jupiter", swe.JUPITER), ("Saturn", swe.SATURN),
                       ("Uranus", swe.URANUS), ("Neptune", swe.NEPTUNE), ("Pluto", swe.PLUTO)]:
        ingresses = find_sign_ingresses(year, pid, name)
        for ing in ingresses:
            lines.append(f"  {ing['planet']:10s} {ing['date']}  {ing['from_sign']} -> {ing['to_sign']}")

    # New & Full Moons
    moons = find_new_full_moons(year)
    lines.append("")
    lines.append("--- NEW & FULL MOONS ---")
    for m in moons:
        lines.append(f"  {m['date']}  {m['type']:10s} at {m['sign']}")

    # Transits to natal chart
    transit_aspects = calc_transits_to_natal(natal, year)
    if transit_aspects:
        lines.append("")
        lines.append("--- TRANSITS TO NATAL CHART ---")
        for t in transit_aspects:
            lines.append(
                f"  {t['month']}  {t['transit_planet']:10s} {t['symbol']} {t['natal_point']:12s} "
                f"({t['aspect']}, orb {t['orb']}°)"
            )
            lines.append(
                f"  {'':6s} Transit: {t['transit_position']}  Natal: {t['natal_position']}"
            )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Astrological Ephemeris Calculator (Swiss Ephemeris)")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Natal chart
    natal_parser = subparsers.add_parser("natal", help="Calculate natal chart")
    natal_parser.add_argument("--date", required=True, help="Birth date (DD.MM.YYYY)")
    natal_parser.add_argument("--time", required=True, help="Birth time (HH:MM)")
    natal_parser.add_argument("--lat", type=float, required=True, help="Latitude")
    natal_parser.add_argument("--lon", type=float, required=True, help="Longitude")
    natal_parser.add_argument("--tz", type=float, default=1.0, help="Timezone offset from UTC (default: 1 for CET)")
    natal_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Transits
    transit_parser = subparsers.add_parser("transits", help="Calculate transits to natal chart")
    transit_parser.add_argument("--date", required=True, help="Birth date (DD.MM.YYYY)")
    transit_parser.add_argument("--time", required=True, help="Birth time (HH:MM)")
    transit_parser.add_argument("--lat", type=float, required=True, help="Latitude")
    transit_parser.add_argument("--lon", type=float, required=True, help="Longitude")
    transit_parser.add_argument("--tz", type=float, default=1.0, help="Timezone offset from UTC")
    transit_parser.add_argument("--year", type=int, required=True, help="Year for transits")
    transit_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Ephemeris
    ephem_parser = subparsers.add_parser("ephemeris", help="Monthly ephemeris")
    ephem_parser.add_argument("--year", type=int, required=True, help="Year")
    ephem_parser.add_argument("--month", type=int, required=True, help="Month (1-12)")
    ephem_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Solar Return
    sr_parser = subparsers.add_parser("solar-return", help="Calculate Solar Return")
    sr_parser.add_argument("--date", required=True, help="Birth date (DD.MM.YYYY)")
    sr_parser.add_argument("--time", required=True, help="Birth time (HH:MM)")
    sr_parser.add_argument("--lat", type=float, required=True, help="Latitude")
    sr_parser.add_argument("--lon", type=float, required=True, help="Longitude")
    sr_parser.add_argument("--tz", type=float, default=1.0, help="Timezone offset")
    sr_parser.add_argument("--year", type=int, required=True, help="Year for Solar Return")
    sr_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Composite
    comp_parser = subparsers.add_parser("composite", help="Composite chart (midpoint)")
    comp_parser.add_argument("--date1", required=True, help="Person 1 birth date (DD.MM.YYYY)")
    comp_parser.add_argument("--time1", required=True, help="Person 1 birth time (HH:MM)")
    comp_parser.add_argument("--lat1", type=float, required=True, help="Person 1 latitude")
    comp_parser.add_argument("--lon1", type=float, required=True, help="Person 1 longitude")
    comp_parser.add_argument("--tz1", type=float, default=1.0, help="Person 1 timezone offset")
    comp_parser.add_argument("--date2", required=True, help="Person 2 birth date")
    comp_parser.add_argument("--time2", required=True, help="Person 2 birth time")
    comp_parser.add_argument("--lat2", type=float, required=True, help="Person 2 latitude")
    comp_parser.add_argument("--lon2", type=float, required=True, help="Person 2 longitude")
    comp_parser.add_argument("--tz2", type=float, default=1.0, help="Person 2 timezone offset")
    comp_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Davison
    dav_parser = subparsers.add_parser("davison", help="Davison relationship chart")
    dav_parser.add_argument("--date1", required=True, help="Person 1 birth date")
    dav_parser.add_argument("--time1", required=True, help="Person 1 birth time")
    dav_parser.add_argument("--lat1", type=float, required=True, help="Person 1 latitude")
    dav_parser.add_argument("--lon1", type=float, required=True, help="Person 1 longitude")
    dav_parser.add_argument("--tz1", type=float, default=1.0)
    dav_parser.add_argument("--date2", required=True, help="Person 2 birth date")
    dav_parser.add_argument("--time2", required=True, help="Person 2 birth time")
    dav_parser.add_argument("--lat2", type=float, required=True, help="Person 2 latitude")
    dav_parser.add_argument("--lon2", type=float, required=True, help="Person 2 longitude")
    dav_parser.add_argument("--tz2", type=float, default=1.0)
    dav_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Progressions
    prog_parser = subparsers.add_parser("progressions", help="Secondary progressions")
    prog_parser.add_argument("--date", required=True, help="Birth date (DD.MM.YYYY)")
    prog_parser.add_argument("--time", required=True, help="Birth time (HH:MM)")
    prog_parser.add_argument("--lat", type=float, required=True, help="Latitude")
    prog_parser.add_argument("--lon", type=float, required=True, help="Longitude")
    prog_parser.add_argument("--tz", type=float, default=1.0)
    prog_parser.add_argument("--age", type=int, required=True, help="Age for progressions")
    prog_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Profection
    prof_parser = subparsers.add_parser("profection", help="Annual profection")
    prof_parser.add_argument("--date", required=True, help="Birth date (DD.MM.YYYY)")
    prof_parser.add_argument("--time", required=True, help="Birth time (HH:MM)")
    prof_parser.add_argument("--lat", type=float, required=True, help="Latitude")
    prof_parser.add_argument("--lon", type=float, required=True, help="Longitude")
    prof_parser.add_argument("--tz", type=float, default=1.0)
    prof_parser.add_argument("--age", type=int, required=True, help="Age for profection")
    prof_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Draconic
    drac_parser = subparsers.add_parser("draconic", help="Draconic chart")
    drac_parser.add_argument("--date", required=True, help="Birth date (DD.MM.YYYY)")
    drac_parser.add_argument("--time", required=True, help="Birth time (HH:MM)")
    drac_parser.add_argument("--lat", type=float, required=True, help="Latitude")
    drac_parser.add_argument("--lon", type=float, required=True, help="Longitude")
    drac_parser.add_argument("--tz", type=float, default=1.0)
    drac_parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.command == "natal":
        chart = natal_chart(args.date, args.time, args.lat, args.lon, args.tz)
        if args.json:
            print(json.dumps(chart, indent=2, ensure_ascii=False))
        else:
            print(format_natal_text(chart))

    elif args.command == "transits":
        chart = natal_chart(args.date, args.time, args.lat, args.lon, args.tz)
        if args.json:
            result = {
                "natal": chart,
                "conjunctions": find_major_conjunctions(args.year),
                "eclipses": find_eclipses(args.year),
                "retrogrades": {},
                "sign_ingresses": {},
                "new_full_moons": find_new_full_moons(args.year),
                "transits_to_natal": calc_transits_to_natal(chart, args.year),
            }
            for name, pid in [("Mercury", swe.MERCURY), ("Venus", swe.VENUS), ("Mars", swe.MARS),
                               ("Jupiter", swe.JUPITER), ("Saturn", swe.SATURN)]:
                result["retrogrades"][name] = find_retrogrades(args.year, pid, name)
            for name, pid in [("Jupiter", swe.JUPITER), ("Saturn", swe.SATURN),
                               ("Uranus", swe.URANUS), ("Neptune", swe.NEPTUNE), ("Pluto", swe.PLUTO)]:
                result["sign_ingresses"][name] = find_sign_ingresses(args.year, pid, name)
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_transits_text(chart, args.year))

    elif args.command == "ephemeris":
        result = monthly_ephemeris(args.year, args.month)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"Ephemeris {args.month:02d}/{args.year}")
            print("-" * 60)
            for day in result["daily"]:
                print(f"\n{day['date']}:")
                for name in PLANETS:
                    if name in day:
                        retro = " (R)" if day[name]["retrograde"] else ""
                        print(f"  {name:12s} {day[name]['position']}{retro}")

    elif args.command == "solar-return":
        sr = solar_return(args.date, args.time, args.lat, args.lon, args.year, args.tz)
        if args.json:
            print(json.dumps(sr, indent=2, ensure_ascii=False))
        else:
            print(f"Solar Return {args.year}")
            print(f"Exact date: {sr['exact_date']} at {sr['exact_time_ut']}")
            print(f"Location: {sr['location']}")
            print("\n--- PLANETS ---")
            for name, data in sr["planets"].items():
                retro = " (R)" if data["retrograde"] else ""
                house = f"  [H{data['house']}]" if "house" in data else ""
                print(f"  {name:12s} {data['formatted']}{retro}{house}")
            print("\n--- ANGLES ---")
            for angle in ("ASC", "MC", "DSC", "IC"):
                print(f"  {angle:12s} {sr['houses'][angle]['formatted']}")

    elif args.command == "composite":
        c1 = natal_chart(args.date1, args.time1, args.lat1, args.lon1, args.tz1)
        c2 = natal_chart(args.date2, args.time2, args.lat2, args.lon2, args.tz2)
        comp = composite_chart(c1, c2, args.lat1, args.lon1)
        if args.json:
            print(json.dumps(comp, indent=2, ensure_ascii=False))
        else:
            print("=" * 60)
            print("  COMPOSITE CHART (Midpoint Method)")
            print("=" * 60)
            print("\n--- PLANETS ---")
            for name, data in comp["planets"].items():
                print(f"  {name:12s} {data['formatted']}")
            print("\n--- ANGLES ---")
            for angle in ("ASC", "MC", "DSC", "IC"):
                print(f"  {angle:12s} {comp[angle]['formatted']}")
            print("\n--- ASPECTS ---")
            for asp in comp["aspects"]:
                print(f"  {asp['planet1']:12s} {asp['symbol']} {asp['planet2']:12s} ({asp['type']}, orb {asp['orb']}°)")

    elif args.command == "davison":
        dav = davison_chart(args.date1, args.time1, args.lat1, args.lon1,
                            args.date2, args.time2, args.lat2, args.lon2,
                            args.tz1, args.tz2)
        if args.json:
            print(json.dumps(dav, indent=2, ensure_ascii=False))
        else:
            print("=" * 60)
            print("  DAVISON RELATIONSHIP CHART")
            print(f"  Midpoint: {dav['midpoint_date']} {dav['midpoint_time_ut']}")
            print(f"  Location: {dav['midpoint_location']}")
            print("=" * 60)
            print("\n--- PLANETS ---")
            for name, data in dav["planets"].items():
                retro = " (R)" if data["retrograde"] else ""
                house = f"  [H{data['house']}]" if "house" in data else ""
                print(f"  {name:12s} {data['formatted']}{retro}{house}")
            print("\n--- ANGLES ---")
            for angle in ("ASC", "MC", "DSC", "IC"):
                print(f"  {angle:12s} {dav['houses'][angle]['formatted']}")

    elif args.command == "progressions":
        prog = progressed_chart(args.date, args.time, args.lat, args.lon, args.age, args.tz)
        if args.json:
            print(json.dumps(prog, indent=2, ensure_ascii=False))
        else:
            print("=" * 60)
            print(f"  SECONDARY PROGRESSIONS - Age {args.age}")
            print(f"  Progressed to: {prog['progressed_date']}")
            print("=" * 60)
            print("\n--- PROGRESSED PLANETS ---")
            for name, data in prog["planets"].items():
                retro = " (R)" if data["retrograde"] else ""
                natal = prog["natal_planets"].get(name, {}).get("formatted", "")
                print(f"  {name:12s} {data['formatted']}{retro}  (natal: {natal})")
            if prog["direction_changes"]:
                print("\n--- DIRECTION CHANGES ---")
                for dc in prog["direction_changes"]:
                    print(f"  {dc['planet']:12s} {dc['change']}")
            if prog["progressed_to_natal_aspects"]:
                print("\n--- PROGRESSED-TO-NATAL ASPECTS ---")
                for asp in prog["progressed_to_natal_aspects"]:
                    print(f"  P.{asp['progressed']:10s} {asp['symbol']} N.{asp['natal']:10s} ({asp['type']}, orb {asp['orb']}°)")

    elif args.command == "profection":
        prof = profection(args.date, args.time, args.lat, args.lon, args.age, args.tz)
        if args.json:
            print(json.dumps(prof, indent=2, ensure_ascii=False))
        else:
            print("=" * 60)
            print(f"  ANNUAL PROFECTION - Age {args.age}")
            print("=" * 60)
            print(f"\n  Activated House  : H{prof['profection_house']}")
            print(f"  Sign             : {prof['profection_sign']}")
            print(f"  Theme            : {prof['theme']}")
            print(f"  Time Lord        : {prof['time_lord']['name']}")
            print(f"  TL natal position: {prof['time_lord']['natal_position']} [H{prof['time_lord']['natal_house']}]")
            retro = " (R)" if prof['time_lord']['retrograde'] else ""
            print(f"  TL retrograde    : {retro.strip() if retro else 'No'}")

    elif args.command == "draconic":
        drac = draconic_chart(args.date, args.time, args.lat, args.lon, args.tz)
        if args.json:
            print(json.dumps(drac, indent=2, ensure_ascii=False))
        else:
            print("=" * 60)
            print(f"  DRACONIC CHART (NN offset: {drac['nn_offset']}°)")
            print("=" * 60)
            print(f"\n{'  Planet':<14s} {'Draconic':<22s} {'Natal':<22s}")
            print(f"  {'-'*56}")
            for name, data in drac["planets"].items():
                print(f"  {name:<12s} {data['formatted']:<22s} {data['natal_position']:<22s}")
            print("\n--- DRACONIC ANGLES ---")
            for angle in ("ASC", "MC", "DSC", "IC"):
                print(f"  {angle:12s} {drac[angle]['formatted']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
