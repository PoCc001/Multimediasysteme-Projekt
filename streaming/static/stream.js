function init_player(streamer){
    fetch("https://api.nictec.net/player/" + streamer)
        .then(response => response.json())
        .then(data => {
            const player = OvenPlayer.create("check-player", data)
        })
}