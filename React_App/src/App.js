import React, {useState, useEffect} from "react";
import Map from './Map';
import Sidebar from './Sidebar';
import './index.css';

function App()   {
  const [event_data, setEvents] = useState(false);
  const [event_types,setTypes] = useState(['mma']);


  const handleChange = (data) =>{
    if (!event_types.includes(data)){
      setTypes(event_types.concat(data))
    }
    else if (event_types.includes(data) ){
      setTypes(event_types.filter(elem => elem !== data))
    };
  };

    
  useEffect(()=> {
      get_db();
  }, [event_types]);


  const get_db = () => {

    fetch('https://fighting-events-api.onrender.com/' + event_types.join('-'))
        .then(response => { 

            return response.text();
        })
        .then(data => {

            setEvents(JSON.parse(data));
        });
  }

  return(
  <div id="sidebar_map">
      <Sidebar event_data = {event_data}/>
      <Map event_data = {event_data} />
      <div id="header">
        <input type="checkbox" value ="mma" checked={event_types.includes("mma")} onChange={() => handleChange("mma")} /> MMA
        <input type="checkbox" value="boxing" onChange={() =>handleChange("boxing")}/> Boxing
      </div>
  </div>
  )

}
export default App