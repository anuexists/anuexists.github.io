with open("assets/js/script.js", "r") as f:
    js = f.read()

# Replace the problematic line with a null check
new_js = js.replace('select.addEventListener("click", function () { elementToggleFunc(this); });', 'if (select) { select.addEventListener("click", function () { elementToggleFunc(this); }); }')

# Replace the innerHTML matching with textContent matching again since we reset it.
new_js = new_js.replace('this.innerHTML.toLowerCase()', 'this.textContent.toLowerCase().trim()')
new_js = new_js.replace('this.innerHTML.trim().toLowerCase()', 'this.textContent.toLowerCase().trim()')

with open("assets/js/script.js", "w") as f:
    f.write(new_js)
