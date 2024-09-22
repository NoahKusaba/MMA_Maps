import { MapContainer, TileLayer, Marker, Popup, useMap, ZoomControl} from 'react-leaflet';
import './map.css'; 
import React, {useEffect} from "react";

const SetFocusMap = ({focus_map}) =>{
  const map = useMap()
  
  useEffect(()=>{
    map.setView(focus_map, map.getZoom(20))
  }, [focus_map])
}
function Map({event_data, focus_map}) {



  return (
    <div id="locations_map">
  
      <MapContainer 
          center={[0,0]}
          zoom={1.5}
          scrollWheelZoom={true} 
          noWrap = {true}
          minZoom={1.5}
          maxBounds ={[[-90,-180],[90,180]]}
          maxBoundsViscosity = {true}>
        <SetFocusMap focus_map = {focus_map}/>

        <TileLayer
         
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
{event_data ? event_data.map((event, idx) => {
          return (

            <Marker position={[event.latitude, event.longitude]} key ={idx} >
            <Popup>
              <div className ='Center'>
                <div>{event.headline} </div> <div>{event.date.split(" ")[0]}  </div>
              </div>
            </Popup>
          </Marker>
          )
        }): "unavailable"}

      </MapContainer>
    </div>
  );
};

export default Map;
