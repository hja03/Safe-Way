function nextMonth() {

    let params = new URLSearchParams(document.location.search);
    let month = parseInt(params.get("month")); 
    let year = parseInt(params.get("year"));

    if (month >= 12) {
        month = 1;
        year += 1
    } else {
        month += 1
    }

    location.replace(`${document.location.pathname}?month=${month}&year=${year}`)
}

function previousMonth() {
    let params = new URLSearchParams(document.location.search);
    let month = parseInt(params.get("month")); 
    let year = parseInt(params.get("year"));

    if (month <= 1) {
        month = 12;
        year -= 1
    } else {
        month -= 1
    }

    location.replace(`${document.location.pathname}?month=${month}&year=${year}`)
}

function changeMode() {
    let params = new URLSearchParams(document.location.search);
    let month = parseInt(params.get("month")); 
    let year = parseInt(params.get("year"));

    if (document.location.pathname == "/ml") {
        location.replace(`/historical?month=${month}&year=${year}`)
    } else {
        location.replace(`/ml?month=${month}&year=${year}`)
    }
}