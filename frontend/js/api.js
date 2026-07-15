const API_BASE = window.location.origin;
console.log("API_BASE =", API_BASE);
console.log("Origin =", window.location.origin);
// const API_URL = "https://paradise-atlas.onrender.com";

export async function getCapitols() {
    const response = await fetch(`${API_BASE}/capitols`);
    return await response.json();
}

export async function getTheatres() {
    const response = await fetch(`${API_BASE}/theatres`);
    return await response.json();
}

export async function getJoelCouldLive() {
    const response = await fetch(`${API_BASE}/joel-could-live`);
    return await response.json();
}

export async function getMichaelCouldLive() {
    const response = await fetch(`${API_BASE}/michael-could-live`);
    return await response.json();
}

export async function getTogetherCouldLive() {
    const response = await fetch(`${API_BASE}/together-could-live`);
    return await response.json();
}

export async function getVisitOrder() {
    const response = await fetch(`${API_BASE}/visit/visit_order`);
    return await response.json();
}

export async function getPatagoniaStores() {
    const response = await fetch(`${API_BASE}/patagonia`);
    return await response.json();
}

export async function getQuakerMeetings() {
    const response = await fetch(`${API_BASE}/quaker-meetings`);
    return await response.json();

}

export async function getLocations() {
    const response = await fetch(`${API_BASE}/locations`);
    return await response.json();

}

export async function getDigs() {
    const response = await fetch(`${API_BASE}/digs/digs_for_map`);
    return await response.json();

}

export async function getVisitedCanadianRailwayHotels() {
    const response = await fetch(`${API_BASE}/canadian_railway_hotels/visited`);
    return await response.json();
}

export async function getNationalParks() {
    const response = await fetch(`${API_BASE}/locations/national_parks`);
    return await response.json();
}