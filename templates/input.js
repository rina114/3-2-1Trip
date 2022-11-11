const form = document.getElementById("form")

form.addEventListener("input", update)
form.addEventListener("change", update)

function update() {
    const isRequired = form.checkValidity()

    if (isRequired) {
    button.style.opacity = 1
    button.style.cursor = "pointer"
    return
    }
}
