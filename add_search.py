from pathlib import Path
import re

# Folder containing your website
folder = Path(".")

# Create the shared search JavaScript file
search_js = """
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
"""

Path("search.js").write_text(search_js, encoding="utf-8")

print("Created search.js")


# Update every HTML page
for file in folder.glob("*.html"):

    # Don't change the Home page because its search already works
    if file.name.lower() == "index.html":
        continue

    text = file.read_text(encoding="utf-8")

    # Find the topbar search box
    pattern = r'<input([^>]*placeholder="[^"]*"[^>]*)>'

    match = re.search(pattern, text, re.IGNORECASE)

    if match:

        input_tag = match.group(0)

        # Only add onkeyup if it doesn't already exist
        if "onkeyup=" not in input_tag.lower():

            new_input = input_tag[:-1] + ' onkeyup="searchPage()">'

            text = text.replace(input_tag, new_input, 1)

            print("Added search to:", file.name)


    # Add search.js before </body>
    if 'src="search.js"' not in text:

        text = text.replace(
            "</body>",
            '<script src="search.js"></script>\n\n</body>'
        )

        print("Connected search.js to:", file.name)


    file.write_text(text, encoding="utf-8")


print("\nDONE!")
print("Search has been added to your HTML pages.")
