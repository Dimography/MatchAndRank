const child_process = require('child_process');
const vk = require('./vk_wrapper');


const pwd = process.env.WD || '/home/Merq/eduhack/stanyslavskysystem';
//const pwd = '/home/Merq/eduhack/stanyslavskysystem';
/**
 * Get possible areas of interest by vk_id
 * @param {string} id vk_id
 * @param {function} done Callback function
 */
const get_areas = (id, done) => {
    console.log('get areas:', id);
    const vk_id = id || '123456';
    const vk_id_re = /[0-9]+/;
    const vk_id_match = vk_id_re.exec(vk_id);

    vk.request('users.get',
        {
            'user_ids': id,
            'fields': 'photo_id,verified,sex,bdate,city,country,home_town,has_photo,photo_50,photo_100,photo_200_orig,photo_200,photo_400_orig,photo_max,photo_max_orig,online,domain,has_mobile,contacts,site,education,universities,schools,status,last_seen,followers_count,occupation,nickname,relatives,relation,personal,connections,exports,wall_comments,activities,interests,music,movies,tv,books,games,about,quotes,can_post,can_see_all_posts,can_see_audio,can_write_private_message,can_send_friend_request,is_favorite,is_hidden_from_feed,timezone,screen_name,maiden_name,crop_photo,is_friend,friend_status,career,military,blacklisted,blacklisted_by_me'
        },
        function (req) {
            if (req.response) {
                console.log(req.response[0]);

                const result_id = req.response[0].id;
                console.log('FOUND ID:', req.response[0].id);

                const process = child_process.exec(
                    'python3 ' + pwd + '/model/predict.py ' + result_id,
                    {
                        cwd: pwd + '/model/'
                    },
                    (err, stdout, stderr) => {
                        if (err) console.error('Exec process error:', err);

                        console.log('Exec result:', stdout);
                        console.error('Exec errror:', stdout);
                        done(err, stdout);
                    }
                );
            }
            else if (vk_id_match[0]) {
                console.log('FOUND ID:', vk_id_match[0]);

                const process = child_process.exec(
                    'python3 ' + pwd + '/model/predict.py ' + vk_id_match[0],
                    {
                        cwd: pwd + '/model/'
                    },
                    (err, stdout, stderr) => {
                        if (err) console.error('Exec process error:', err);

                        console.log('Exec result:', stdout);
                        console.error('Exec errror:', stdout);
                        done(err, stdout);
                    }
                );
            }
            else {
                console.log('user not found');
                done(new Error('Не могу найти пользователя с таким id'), {});
            }
        }
    );
};

/**
 * Get possible tutors by vk_id
 * @param {string} id vk_id
 * @param {function} done Callback function
 */
const get_tutors = (id, done) => {
    const vk_id = id || '323627';

    const process = child_process.exec(

        //'python3 ' + pwd + '/model/model.py -id ' + vk_id,
        'pwd',
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
