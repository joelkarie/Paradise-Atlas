import { createMap } from "./map.js";
import { createTheatreLayer } from "./layers/theatres.js";
import { getTheatres } from "./api.js";
import { createCapitolLayer } from "./layers/capitol.js";
import { getCapitols } from "./api.js";
import { createCouldLiveLayer } from "./layers/could_live.js";
import { getJoelCouldLive, getMichaelCouldLive, getTogetherCouldLive } from "./api.js";
import { createVisitOrderLayer } from "./layers/visit_order.js";
import { getVisitOrder } from "./api.js";
import { createPatagoniaStoreLayer } from "./layers/patagonia_stores.js";
import { getPatagoniaStores } from "./api.js";
import { createQuakerMeetingsLayer } from "./layers/quaker_meetings.js";
import { getQuakerMeetings } from "./api.js";
import { getLocations } from "./api.js";
import { createLocationsLayer } from "./layers/locations.js";



async function main() {

    const map = createMap();


    const theatreLayer = createTheatreLayer(await getTheatres());
    const capitolLayer = createCapitolLayer(await getCapitols(), "capitol_marker_2.png");
    const joelCouldLiveLayer = createCouldLiveLayer(await getJoelCouldLive(), "joel_in_dot_gray_2.png");
    const michaelCouldLiveLayer = createCouldLiveLayer(await getMichaelCouldLive(), "michael_h.png");
    const togetherCouldLiveLayer = createCouldLiveLayer(await getTogetherCouldLive(), "together_gold_dot_2.png", "65")
    const patagoniaStoreLayer = createPatagoniaStoreLayer(await getPatagoniaStores());
    const vistitOrderLayer = createVisitOrderLayer(await getVisitOrder());
    const quakerMeetingHouseLayer = createQuakerMeetingsLayer(await getQuakerMeetings());
    const locationLayer = createLocationsLayer( await getLocations());

    locationLayer.addTo(map)

    const overlays = {
        "Locations Visited": locationLayer,
        "Visit Order": vistitOrderLayer,
        "Theatres We Have Worked At": theatreLayer,
        "Capitols Visited": capitolLayer,
        "Cities Michael Could Live In": michaelCouldLiveLayer,
        "Cities Joel Could Live In": joelCouldLiveLayer,
        "Cities We Both Could Live In": togetherCouldLiveLayer,
        "Patagonia Stores": patagoniaStoreLayer,
        "Quaker Meetings Houses Attended": quakerMeetingHouseLayer
    };

    L.control.layers(null, overlays).addTo(map);

}

main();