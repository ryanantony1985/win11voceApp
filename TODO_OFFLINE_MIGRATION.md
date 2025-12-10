# TODO: Migrate VoiKy to Fully Offline Speech Recognition

## Objective

Replace Google Web Speech API with a fully offline speech recognition engine (Vosk or Whisper) while maintaining all current functionality.

## Current Functionality to Preserve

- [x] Real-time voice-to-text conversion
- [x] Background listening mode
- [x] Automatic text injection into active applications
- [x] Minimal UI with start/stop controls
- [x] Ambient noise adjustment
- [x] Error handling for unintelligible speech

## Migration Tasks

### Research & Planning

- [ ] Evaluate Vosk vs Whisper for offline speech recognition
  - [ ] Compare accuracy, speed, and resource usage
  - [ ] Check Windows compatibility
  - [ ] Verify model sizes and download requirements
  - [ ] Test real-time streaming capabilities
- [ ] Select the best offline engine for VoiKy's use case
- [ ] Document migration approach and architecture changes

### Implementation

- [ ] Update `requirements.txt` with new speech recognition library
- [ ] Download and bundle appropriate language model(s)
- [ ] Refactor `core/speech_handler.py` to use offline engine
  - [ ] Replace `recognize_google()` with offline recognition
  - [ ] Maintain background listening functionality
  - [ ] Preserve ambient noise adjustment
  - [ ] Keep error handling structure
- [ ] Update PyInstaller spec to include model files in build
- [ ] Test real-time performance and accuracy

### Privacy & Documentation

- [ ] Update `PRIVACY_POLICY.txt` to reflect fully offline operation
  - [ ] Remove Google API references
  - [ ] Confirm no internet transmission
  - [ ] Update third-party services section
- [ ] Update `README.md` with offline capabilities
- [ ] Document model download/setup process if needed

### Testing & Verification

- [ ] Test voice recognition accuracy
- [ ] Verify background listening works correctly
- [ ] Test text injection into various applications
- [ ] Confirm no internet connection required
- [ ] Test EXE build includes all model files
- [ ] Verify MSIX package works with bundled models

### Build & Distribution

- [ ] Update build scripts if model files need special handling
- [ ] Test final MSIX package size (models may be large)
- [ ] Verify Windows Store submission with larger package
- [ ] Update app description to highlight offline capability

## Prompt for Antigravity

```
Migrate VoiKy from Google Web Speech API to a fully offline speech recognition solution. 

Current implementation uses `speech_recognition` library with `recognize_google()` in `core/speech_handler.py`. 

Requirements:
1. Replace with Vosk or Whisper (evaluate both, recommend best option)
2. Maintain all current functionality:
   - Real-time background listening
   - Text injection into active apps
   - Ambient noise adjustment
   - Error handling
3. Ensure models are bundled in PyInstaller build
4. Update privacy policy to reflect fully offline operation
5. Keep the same UI and user experience

Please analyze the current code, recommend the best offline engine, and implement the migration while preserving all functionality.
```
