chrome.runtime.onConnect.addListener(function (port) {
    if (port.name === "padding password") {

        port.onMessage.addListener(function (message) {
            if (message.event === "padding password") {
                document.getElementById("username").value = message.username;
                document.getElementById("P_model").value = message.password;
                document.getElementById("button").click();
            }
            port.postMessage({
                content: "OK"
            });
            //port.disconnect();
        });
    };
})