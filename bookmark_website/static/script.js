function copyToClipboard(url) {
    navigator.clipboard.writeText(url).then(() => alert("Copied: " + url));
}

// Drag and drop: simple copy URL to external apps
function drag(ev) {
    ev.dataTransfer.setData("text/plain", ev.target.dataset.url);
}

// Optional: auto-refresh every 30s
setInterval(() => { location.reload(); }, 30000);
