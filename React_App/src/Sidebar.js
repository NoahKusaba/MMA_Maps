import './sidebar.css';
function Sidebar({event_data, setFocusMap} ) {

  return (
    <div id="sidebar">
      
      {event_data ? event_data.map((event,idx) =>{
        return(
          <div className  ="sidebar_row"  key ={idx}>

            <a href ={event.url} className="imageCont"> <img alt="org" className={event.org}/> </a>
            <a href= {event.url} className="event">
              {event.headline} <br/> 
              {event.date.split(" ")[0]}
            </a> 
            <img alt='map' className='mapIcon' 
            onClick={ () => setFocusMap([event.latitude, event.longitude])} />
          </div>
        )
      }): "unavailable"}
    </div>

  );
}
export default Sidebar;