async function connectToDevice() {
    try {
        // Replace '20:1e:88:18:14:ff' with the UUID of the Bluetooth device
        const device = await navigator.bluetooth.requestDevice({
            filters: [{ services: ['20:1e:88:18:14:ff'] }]
        });

        const server = await device.gatt.connect();
        const service = await server.getPrimaryService('20:1e:88:18:14:ff'); // Use the UUID directly for the service
        const characteristics = await service.getCharacteristics();
        
        // Find the characteristic you want to use
        const characteristic = characteristics.find(char => char.properties.write);

        if (characteristic) {
            // Send data when button is clicked
            document.getElementById('connectButton').addEventListener('click', async () => {
                const textToSend = "Hello, Bluetooth World!"; // Example text
                const encoder = new TextEncoder();
                const encodedData = encoder.encode(textToSend);
                await characteristic.writeValue(encodedData);
                console.log('Data sent over Bluetooth:', textToSend);
            });
        } else {
            console.error('No writable characteristic found.');
        }

    } catch (error) {
        console.error('Bluetooth error:', error);
    }
}

document.getElementById('connectButton').addEventListener('click', connectToDevice);