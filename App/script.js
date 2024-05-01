async function connectToDevice() {
    try {
        const device = await navigator.bluetooth.requestDevice({
            acceptAllDevices: true
        });

        const server = await device.gatt.connect();
        
        // Discover services
        const services = await server.getPrimaryServices();
        
        // Loop through services to find desired characteristic
        for (const service of services) {
            const characteristics = await service.getCharacteristics();
            for (const characteristic of characteristics) {
                // Check for characteristic properties you expect
                if (characteristic.properties.write) {
                    // If it's writable, use it
                    const value = await characteristic.readValue();
                    console.log('Characteristic UUID:', characteristic.uuid);
                    console.log('Value:', value);
                    // Send data when button is clicked
                    document.getElementById('connectButton').addEventListener('click', async () => {
                        const textToSend = "Hello, Bluetooth World!"; // Example text
                        const encoder = new TextEncoder();
                        const encodedData = encoder.encode(textToSend);
                        await characteristic.writeValue(encodedData);
                        console.log('Data sent over Bluetooth:', textToSend);
                    });
                    return; // Exit after finding the first writable characteristic
                }
            }
        }
        
        console.error('No writable characteristic found.');

    } catch (error) {
        console.error('Bluetooth error:', error);
    }
}

document.getElementById('connectButton').addEventListener('click', connectToDevice);
