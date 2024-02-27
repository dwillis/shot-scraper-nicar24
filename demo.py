import subprocess
import json

def fetch_and_parse_byu(season):
    name = 'Brigham Young'
    ncaa_id = 77

    # JavaScript to be executed by shot-scraper
    javascript_code = """
    Array.from(document.querySelectorAll('.roster__players .roster-card-item'), el => {
     const id = '';
     const name = el.querySelector('a').innerText;
     const year = el.querySelectorAll('.roster-player-card-profile-field')[0].querySelectorAll('span')[1].innerText;
     const height = el.querySelectorAll('.roster-player-card-profile-field')[0].querySelectorAll('span')[0].innerText;
     const position = el.querySelector('.roster-card-item__position').innerText;
     const hometown = el.querySelector(".roster-player-card-profile-field__value--hometown").innerText;
     hs_el = el.querySelector(".roster-player-card-profile-field__value--previous-school");
     const high_school = hs_el ? hs_el.innerText : '';
     const previous_school = '';
     const jersey = el.querySelector(".roster-card-item__jersey-number").innerText;
     const url =el.querySelector("a")['href'];
     return {id, name, year, hometown, high_school, previous_school, height, position, jersey, url};
    })
    """

    roster = []
    url = "https://byucougars.com/sports/womens-basketball/roster/season/" + season
    # Execute shot-scraper with the given JavaScript
    try:
        result = subprocess.check_output(['shot-scraper', 'javascript', url, javascript_code, "--user-agent", "Firefox"])
        parsed_data = json.loads(result)

        for player in parsed_data:
            player['team_id'] = ncaa_id
            player['team'] = name
            player['season'] = season

        return parsed_data
    except:
        raise

# Maryland { "team": "Maryland", "url": "https://umterps.com/sports/womens-basketball", "ncaa_id": 392 }
# Drexel { "team": "Drexel", "url": "https://drexeldragons.com/sports/womens-basketball", "ncaa_id": 191}
# [9, 71, 83, 96, 99, 156, 173, 180, 191, 234, 249, 257, 301, 306, 367, 387, 392, 400, 404, 418, 428, 441, 490, 521, 522, 559, 574, 603, 635, 664, 671, 676, 688, 690, 700, 719, 749, 758]:
def shotscraper_card(team, season):
    ncaa_id = team['ncaa_id']
    name = team['team']

    # JavaScript to be executed by shot-scraper
    javascript_code = """
    Array.from(document.querySelectorAll('.s-person-card__content'), el => {
        const id = '';
        const name = el.querySelector('.s-person-details__personal-single-line').innerText;
        const year = el.querySelectorAll('.s-person-details__bio-stats-item')[1].childNodes[1].wholeText.trim();
        let ht = el.querySelectorAll('.s-person-details__bio-stats-item')[2].childNodes[1].wholeText;
        const height = ht ? ht.trim() : '';
        const position = el.querySelectorAll('.s-person-details__bio-stats-item')[0].childNodes[1].textContent.trim()
        const hometown = el.querySelectorAll('.s-person-card__content__person__location-item')[0].childNodes[2].textContent.trim();
        let hs_el = el.querySelectorAll('.s-person-card__content__person__location-item')[1].childNodes[1].textContent;
        const high_school = hs_el ? hs_el.trim() : '';
        const previous_school = '';
        let j = el.querySelector('.s-stamp__text');
        const jersey = j ? j.innerText : '';
        const url = el.querySelector('a')['href']
        return {id, name, year, hometown, high_school, previous_school, height, position, jersey, url};
    })
    """

    roster = []
    url = team['url'] + "/roster/" + season
    # Execute shot-scraper with the given JavaScript
    try:
        result = subprocess.check_output(['shot-scraper', 'javascript', url, javascript_code, "--user-agent", "Firefox"])
        parsed_data = json.loads(result)

        for player in parsed_data:
            player['team_id'] = ncaa_id
            player['team'] = name
            player['season'] = season

        return parsed_data
    except:
        raise