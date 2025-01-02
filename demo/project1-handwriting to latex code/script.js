let conversionCount = 0;
const FREE_CONVERSION_LIMIT = 5;

// Function to handle image upload and OCR
async function convertImageToLatex() {
    const imageInput = document.getElementById('imageUpload');
    const latexOutput = document.getElementById('latexOutput');
    const conversionCountElement = document.getElementById('conversionCount');

    if (!imageInput.files[0]) {
        alert("Please upload an image file.");
        return;
    }

    if (conversionCount >= FREE_CONVERSION_LIMIT) {
        alert("You have reached the free conversion limit. Please subscribe for unlimited access.");
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);

    try {
        const response = await fetch('https://api.ocr.space/parse/image', {
            method: 'POST',
            headers: {
                'apikey': 'K85612807788957',
            },
            body: formData,
        });

        const data = await response.json();
        if (data.ParsedResults && data.ParsedResults[0].ParsedText) {
            const rawText = data.ParsedResults[0].ParsedText;

            // Parse raw text to LaTeX (basic transformation)
            const latexCode = rawText.replace(/\*/g, '\\cdot ').replace(/ /g, '\\ ');
            latexOutput.value = latexCode;

            conversionCount++;
            conversionCountElement.textContent = `Conversions used: ${conversionCount} / ${FREE_CONVERSION_LIMIT}`;
        } else {
            latexOutput.value = "Error: Could not extract text.";
        }
    } catch (error) {
        console.error("Error during OCR:", error);
        latexOutput.value = "Error: Unable to process the image.";
    }
}

// Attach event listener to button
const convertButton = document.getElementById('convertButton');
convertButton.addEventListener('click', convertImageToLatex);

// Subscription feature
const subscribeButton = document.getElementById('subscribeButton');
subscribeButton.addEventListener('click', () => {
    alert("Thank you for subscribing! Unlimited conversions are now enabled.");
    conversionCount = -1; // Disable limit
    document.getElementById('conversionCount').textContent = "Unlimited conversions enabled.";
});