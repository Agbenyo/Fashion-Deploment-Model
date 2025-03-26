# API Reference

## Root Endpoint

### `GET /`

Returns a welcome message.

**Response:**
- 200 OK
- JSON format: `{ "message": "Welcome to the CNN Project!" }`

## Train Model

### `POST /train`

Trains the model.

**Body**:
- `dataset`: Path to the training dataset.

**Response:**
- 200 OK
- JSON format: `{ "status": "Training complete" }`

## Predict

### `POST /predict`

Generates predictions based on the input image.

**Body**:
- `image`: Base64 encoded image data.

**Response:**
- 200 OK
- JSON format: `{ "predictions": [...] }`
