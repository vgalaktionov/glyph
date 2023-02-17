import * as ROT from "rot-js";

const display = new ROT.Display({ width: 40, height: 9, layout: "term" });

display.draw(5, 4, "@", null, null);
display.draw(15, 4, "%", "#0f0", null); // foreground color
display.draw(25, 4, "#", "#f00", "#009"); // and background color
