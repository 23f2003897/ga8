# Question 2: GCP Gemini API Math Puzzle

## Objective
Integrate with the Google Gemini API to solve a unique math puzzle and return structured JSON output for verification.

## Unique Puzzle
"Start with 2, multiply by 3, subtract 2, then divide by 2"

## Troubleshooting & Learning Trace
During development, I encountered and resolved the following technical challenges:
1. **API Versioning (404 Error):** Resolved by listing available models using `client.models.list()` to identify the correct model strings for the `google-genai` library.
2. **Rate Limiting (429 Error):** Encountered "Resource Exhausted" limits on the Free Tier for `gemini-3.1-pro`.
3. **Server Congestion (503 Error):** Handled "High Demand" errors by attempting failover to stable models like `gemini-1.5-flash` and `gemini-pro-latest`.

## Final Result
- **Answer:** 2
- **Steps Count:** 3
- **Verification Hash:** c09890a8a81639