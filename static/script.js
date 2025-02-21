function legacyCopy(text) {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
}
function codeCopy() {
    document.querySelectorAll("code").forEach((codeBlock) => {
        codeBlock.style.cursor = "pointer";
        codeBlock.addEventListener("click", function () {
            const text = this.innerText;
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(text).then(() => {
                    this.classList.add("copied");
                    this.style.setProperty("background-color", "#e0e0e0", "important");
                    this.style.setProperty("color", "black", "important");
                    const computedStyle = window.getComputedStyle(this);
                    setTimeout(() => {
                        this.classList.remove("copied");
                        this.style.setProperty("background-color", "", "important");
                        this.style.setProperty("color", "", "important");
                        const computedStyleAfter = window.getComputedStyle(this);
                    }, 1000);
                }).catch(err => {
                    legacyCopy(text);
                });
            } else {
                legacyCopy(text);
            }
        });
    });
}

document.addEventListener("DOMContentLoaded", codeCopy);
