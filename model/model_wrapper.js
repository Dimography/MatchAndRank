const child_process = require('child_process');


/**
 * Get possible areas of interest by vk_id
 * @param {string} id vk_id
 * @param {function} done Callback function
 */
const get_areas = (id, done) => {
    const vk_id = id || '123456';

    const process = child_process.exec(
        'python ./model.py -id ' + vk_id,
        (err, stdout, stderr) => {
            if (err) console.error('Exec process error:', err);

            console.log('Exec result:', stdout);
            console.error('Exec errror:', stdout);
            done(err, { areas: [] });
        }
    );
};

/**
 * Get possible tutors by vk_id
 * @param {string} id vk_id
 * @param {function} done Callback function
 */
const get_tutors = (id, done) => {
    const vk_id = id || '123456';

    const process = child_process.exec(
        'python ./model.py -id ' + vk_id,
        (err, stdout, stderr) => {
            if (err) console.error('Exec process error:', err);

            console.log('Exec result:', stdout);
            console.error('Exec errror:', stdout);
            done(err, { areas: [] });
        }
    );
};

module.exports = {
    get_areas: get_areas,
    get_tutors: get_tutors
}
