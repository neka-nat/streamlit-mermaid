import React, { useRef, useEffect, ReactElement } from "react";
import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib";
import mermaid from "mermaid";
import svgPanZoom from "svg-pan-zoom";

function MermaidViwer({ args }: ComponentProps): ReactElement {
  const ref = useRef<HTMLDivElement>(null);
  const { code, width, height, pan, zoom, show_controls } = args;

  useEffect(() => {
    Streamlit.setFrameHeight();
  });

  useEffect(() => {
    if (ref.current) {
      mermaid.mermaidAPI.render("graphDiv", code).then((svgGraph) => {
        if (ref.current) {
          ref.current.innerHTML = svgGraph.svg;

          if (pan || zoom) {
            svgPanZoom("#graphDiv", {
              viewportSelector: ".svg-pan-zoom_viewport",
              panEnabled: pan,
              controlIconsEnabled: show_controls,
              zoomEnabled: zoom,
              dblClickZoomEnabled: zoom,
              mouseWheelZoomEnabled: zoom,
              preventMouseEventsDefault: true,
              zoomScaleSensitivity: 0.2,
              minZoom: 0.5,
              maxZoom: 10,
              fit: true,
              contain: false,
              center: false,
              refreshRate: "auto",
            });
          }
          
          var graph = document.getElementById("graphDiv");
          if (graph) {
            var svgs = document.getElementsByClassName("svg-pan-zoom_viewport");
            if (svgs.length > 0) {
            var svg = svgs[0];
            var bbox = svg.getBoundingClientRect();
          } else {
            bbox = graph.getBoundingClientRect();
          }
          graph.setAttribute("height", "" + (bbox.height + 16));
          if (height === "auto") {
            Streamlit.setFrameHeight(bbox.height + 16);
          }
        }
      }
      });
    }
  }, [code, height, pan, zoom, show_controls]);

  return (
    <div
      ref={ref}
      style={{ width: width, height: height, overflow: "auto" }}
    ></div>
  );
}

export default withStreamlitConnection(MermaidViwer);
