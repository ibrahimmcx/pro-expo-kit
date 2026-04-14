# Reanimated Yerine Animated API Kullanımı

## Context
- **SDK**: 54
- **Trigger**: Animasyon yapılması gerektiğinde Reanimated karmaşasından kaçınma.

## Problemler
- Reanimated native konfigürasyon hataları.
- Babel plugin çakışmaları.
- "Runtime not ready" hataları.

## Çözüm
React Native'in yerleşik `Animated` API'sini kullanın. Native driver (`useNativeDriver: true`) kullanıldığı sürece performans oldukça iyidir.

## Kod Örneği
```javascript
import { Animated } from 'react-native';

// Değer tanımlama
const fadeAnim = useRef(new Animated.Value(0)).current;

// Başlatma
Animated.timing(fadeAnim, {
  toValue: 1,
  duration: 500,
  useNativeDriver: true,
}).start();

// JSX
<Animated.View style={{ opacity: fadeAnim }}>
  <Text>Pürüzsüz Animasyon</Text>
</Animated.View>
```
