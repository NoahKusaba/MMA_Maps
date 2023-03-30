import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import './map.css';


function Map({event_data}) {

  return (
    <div id="locations_map">
  
      <MapContainer 
          center={[0,0]} 
          zoom={2} 
          scrollWheelZoom={true} 
          noWrap = {true}

          maxNativeZoom={2}
          maxBounds ={[[-90,-180],   [90,180]] }
          maxBoundsViscosity = {true}>
        <TileLayer

          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
{event_data ? event_data.map((event, idx) => {
          return (

            <Marker position={[event.latitude, event.longitude]} key ={idx} >
            <Popup>
              {event.headline} <br /> {event.date.split(" ")[0]}     
            </Popup>
          </Marker>
          )
        }): "unavailable"}

      </MapContainer>
    </div>
  );
};

export default Map;
