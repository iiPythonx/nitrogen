// Copyright 2022 iiPython

const socket = io();
socket.on("connect", () => {
    console.log("Connected to Nitrogen socket.io!");
});

const emit = (fn, ...args) => {
    socket.emit(fn, args);
    console.log("Sent event to server!");
}
const on = socket.on;
