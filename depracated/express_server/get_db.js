const Pool = require("pg").Pool
const pool = new Pool({
    user: "noahk",
    host: "localhost",
    database: "event_maps",
    password: "projectmap",
    port: 5432
});
// putting db information in file is not recommended for production. 

// we only care about getfunction
const get_db = () => {
    return new Promise(function(resolve, reject) {
        pool.query("select * from mma", (error,results) => {
            if (error) {
                reject(error)
            }
            resolve(results.rows);
        })
    })
}


module.exports = {
    get_db,
}