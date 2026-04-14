# Expo SDK 54 Core Skill

This skill contains the "hard facts" and best practices for developing on **Expo SDK 54**.

## 🚀 Version Map (Pin These)

| Package | Version Range |
| :--- | :--- |
| `expo` | `~54.0.0` |
| `react-native` | `0.77.x` |
| `expo-router` | `~4.0.0` |
| `expo-status-bar` | `~2.0.0` |

## 💡 Best Practices

1. **New Architecture**: SDK 54 is the bridge. Always check if a library supports the New Architecture (TurboModules) if you have it enabled.
2. **Prebuild**: Use `npx expo prebuild` to see native changes. 
3. **Animations**: DO NOT use Reanimated. Rely on `Animated` API.
4. **Icons**: Use `@expo/vector-icons` which is built-in.

## 🛠️ Common Fixes (SDK 54)

- **Manifest Error**: Ensure `expo-updates` is configured.
- **Gradle Version**: Ensure Java 17+ for Android builds.
- **Metro Config**: Use the modern `metro.config.js` skeleton provided by `expo/metro-config`.
