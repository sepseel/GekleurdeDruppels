var staat = {};
var grid = false;
const url = "http://users.ugent.be/~sevbesau/cgi-bin/script.cgi?";
//var url = "http://0.0.0.0:8080/cgi-bin/script.cgi?";



update = function(state) {
    // als er nog geen grid van divs bestaat, maak er dan een
    if (!grid) {
        makeGrid(state.board.length);
        grid = true;
    }

    // spelbord updaten
    for (let i = 0; i < state.board.length; i++) {
        for (let j = 0; j < state.board.length; j++) {
            $('#' + i + "" + j).css('background', state.board[i][j])
        }
    }

    // zetten updaten
    let kleuren = ['#green', '#red', '#orange', '#blue', '#purple'];
    for (let kleur of kleuren) {
        $(kleur).hide()
    }
    for (let move of state.moves) {
        $('#' + move).show()
    }
    $("#colour").val("gray");

    // score updaten
    $('#score').text('score: ' + state.score)

    // als er een bericht is, geef het dan weer
    if (state.message) {
        alert(state.message);
    }

    // state opslagen als stringweergave
    staat = JSON.stringify(state)
}

makeGrid = function(n) {
    // maakt een leeg div grid aan met het opgegeven aantal rijen en kolommen
    grid = true;
    for (let i = 0; i < n; i++) {
        $(".rooster").append("<div id='row" + i + "'></div>")
        for (let j = 0; j < n; j++) {
            $("#row" + i).append("<div id='" + i + "" + j + "' class='circle'></div>")
        }
    }
}

Startnew = function() {
    // start een nieuw spel
    fetch(url + "new_game")
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
        update(myJson);
        console.log('new', myJson)
    });

}

maakZet = function(staat, kleur) {
    // maakt een zet op basis van de opgeslagen staat en de geselecteerde kleur

    fetch(url + 'do_move=' + staat + '+' + kleur)
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
        update(myJson);
        //console.log(myJson)
    });
};

function setColours(){
    var cur_kleur = $(".color").val();
    $(".color").css("background-color", cur_kleur);
}



makeGrid(5);
Startnew();
$(document).ready(function(){
    // word uitgevoerd wanneer alle html geladen is

    $(".color").change(function(){
      setColours();
    });

    $('#00').click(function(){
        let kleur = $('#colour').val()
        //console.log(kleur)
        if (kleur != 'gray') {
            maakZet(staat, "'" + kleur + "'");
        }
        $('.color').css('background-color', 'gray')
    })

    $('#new').click(function(){
        Startnew();
    });

});
