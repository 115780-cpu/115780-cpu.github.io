function searchPage() {

    var searchBox = document.querySelector(".topbar input");

    if (!searchBox) {
        return;
    }

    var searchText = searchBox.value.toLowerCase().trim();

    var cards = document.querySelectorAll(".card");

    cards.forEach(function(card) {

        var text = card.innerText.toLowerCase();

        if (text.includes(searchText)) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }

    });

}