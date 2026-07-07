// const API_URL = "http://localhost:8000";
const API_URL = "https://paradise-atlas.onrender.com";

export async function getCapitols() {
    const response = await fetch(`${API_URL}/capitols`);
    return await response.json();
}

export async function getTheatres() {
    const response = await fetch(`${API_URL}/theatres`);
    return await response.json();
}

export async function getJoelCouldLive() {
    const response = await fetch(`${API_URL}/joel-could-live`);
    return await response.json();
}

export async function getMichaelCouldLive() {
    const response = await fetch(`${API_URL}/michael-could-live`);
    return await response.json();
}

export async function getTogetherCouldLive() {
    const response = await fetch(`${API_URL}/together-could-live`);
    return await response.json();
}

export async function getVisitOrder() {
    const response = await fetch(`${API_URL}/visit/visit_order`);
    return await response.json();
}

export async function getPatagoniaStores() {
    const response = await fetch(`${API_URL}/patagonia`);
    return await response.json();
}

export async function getQuakerMeetings() {
    const response = await fetch(`${API_URL}/quaker-meetings`);
    return await response.json();

}

export async function getLocations() {
    const response = await fetch(`${API_URL}/locations`);
    return await response.json();

}

export async function getDigs() {
    const response = await fetch(`${API_URL}/digs/digs_for_map`);
    return await response.json();

}

export async function getVisitedCanadianRailwayHotels() {
    const response = await fetch(`${API_URL}/canadian_railway_hotels/visited`);
    return await response.json();
}