import React, {useState, useEffect} from "react";
import Map from './Map';
import Sidebar from './Sidebar'
import './index.css';

function App()   {
    const [event_data, setEvents] = useState(false);
    // const [event_type, setType]= useState(true);

    useEffect(()=> {
        get_db();
    }, []);

    function get_db() {
        fetch('https://fighting-events-api.onrender.com/mma')
            .then(response => { 
                console.log(response)
                return response.text();
            })
            .then(data => {
                
                console.log(data)
                setEvents(JSON.parse(data));
            });
    }
    console.log(event_data[0])
    return(
    <div id="sidebar_map">
        <Sidebar event_data = {event_data}/>
        <Map event_data = {event_data} />
    </div>
    )

}
export default App