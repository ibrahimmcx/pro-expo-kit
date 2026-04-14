# Expo SDK 54 Versiyon Sabitleme (Pinning)

## Context
- **SDK**: 54
- **Trigger**: Yeni kütüphane eklerken versiyon uyumsuzlukları.

## Problemler
- `npx expo install` dışında `npm install` kullanıldığında SDK dışı paketlerin yüklenmesi.
- Gradle build hataları.

## Çözüm
Her zaman `npx expo install` komutunu kullanın. Bu komut SDK 54 ile uyumlu olan en yakın versiyonu otomatik seçer.

**package.json kontrol listesi:**
- `expo`: `~54.0.0`
- `react-native`: `0.77.x`
- `expo-router`: `~4.0.0`

## Command
```bash
# Bir paket eklerken:
npx expo install firebase
# Tüm paketleri valide etmek için:
npx expo install --check
```
