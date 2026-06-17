import { createMap } from "./map.js";
import { createTheatreLayer } from "./layers/theatres.js";
import { getTheatres } from "./api.js";
import { createCapitolLayer } from "./layers/capitol.js";
import { getCapitols } from "./api.js";
import { createJoelCouldLiveLayer } from "./layers/joel_could_live.js";
import { getJoelCouldLive } from "./api.js";
import { createVisitOrderLayer } from "./layers/visit_order.js";
import { getVisitOrder } from "./api.js";


async function main() {

    const map = createMap();


    const theatreLayer = createTheatreLayer(await getTheatres());
    const capitolLayer = createCapitolLayer(await getCapitols());
    const joelCouldLiveLayer = createJoelCouldLiveLayer(await getJoelCouldLive());
    const vistitOrderLayer = createVisitOrderLayer(await getVisitOrder());

    const overlays = {
        "Locations Visited": vistitOrderLayer,
        "Theatres We Have Worked At": theatreLayer,
        "Capitols Visited": capitolLayer,
        "Cities Joel Could Live In": joelCouldLiveLayer
    };

    L.control.layers(overlays).addTo(map);

}

main();