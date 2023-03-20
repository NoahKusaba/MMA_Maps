import './sidebar.css';
function Sidebar({event_data}) {
  return (
    <div id="sidebar">
      
      {event_data ? event_data.map((event,idx) =>{
        return(
          <div className  ="sidebar_row"  key ={idx}>
            <img alt="org" className={event.org}/>
            <div className="event">
              {event.headline} <br/> 
              {event.date.split(" ")[0]}
            </div> 
          </div>
        )
      }): "unavailable"}
    </div>

  );
}
export default Sidebar;