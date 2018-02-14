const model_wrapper = require('./model_wrapper');

model_wrapper.get_areas('323627', (err, stdout) => {
    console.log(err);
});


module.exports = model_wrapper;