/**
 * Created by ramezashraf on 11/5/15.
 */

$(document).ready(function () {

    $('div.simple-review-raty').each(function (i, elem) {
        // get next forminput for default value & setting sciornName
        var $elem = $(elem);
        var score = $elem.attr('data-score');
        var score_name = $elem.attr('scoreName');

        var settings = {
            score: score
        };
        if (!score_name) {
            settings.readOnly = true;
        } else {
            settings.scoreName = score_name;
        }
        $elem.raty(settings)

    })
})
;
