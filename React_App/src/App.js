import React, {useState, useEffect} from "react";
import Map from './Map';
import Sidebar from './Sidebar';
import './app.css';

function App()   {
  const [event_data, setEvents] = useState(false);
  const [focus_map, setFocusMap] = useState([0,0]);
  // const focus_map = [0,0]
  const [event_types,setTypes] = useState(['mma']);
  const total_types = ["mma", "boxing","judo","bjj"]

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
      <Sidebar event_data = {event_data} setFocusMap ={setFocusMap}  />
      <Map event_data = {event_data} focus_map = {focus_map}  />
      <div id="header">
        {total_types.map((event_name,idx) => {
          return(
            <div className = "checkbox" key={idx}>
              {event_name.toUpperCase()}
              <input type="checkbox" value ={event_name} checked={event_types.includes(event_name)} onChange={() => handleChange(event_name)} /> 
            </div>
          )
          
        })}

      </div>
  </div>
  )

}
export default App