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

export async function getVisitOrder() {
    const response = await fetch(`${API_URL}/visit-order`);
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