# SPEAK DAY — Forest Edition

A standalone Node.js vocabulary-learning website. It contains all 721 English words and their source English definitions from the supplied NGSL Spoken list.

## Run
- Node.js 18+
- `npm start`
- Open the provided local/deployed URL.

## Features
- 37-day course (20 words per day; final day has one word)
- Browser US-English pronunciation via SpeechSynthesis
- Know / Don't know tracking and spaced review schedule
- Local browser progress storage
- Copy today's vocabulary and a ChatGPT conversation prompt
- Forest palette: sage green, warm beige, soft lavender

## Notes
- Progress is stored in the current browser's localStorage, not cloud-synced.
- Pronunciation uses the device/browser's available English voice; it is not a studio-recorded native-speaker recording.
- The source dataset contains 721 English headwords and English definitions. Korean glosses are currently included for common words; entries without a verified Korean gloss display a notice rather than a guessed translation.
- Word illustrations use semantic emoji/icon cues rather than 721 individually commissioned images.


## 한국어 뜻 및 그림 보강 안내
- words.json의 721개 항목 모두에 meaning_ko 필드를 추가했습니다.
- 자주 쓰이는 단어는 한국어 핵심 뜻을 직접 정리했고, 나머지는 정의문 패턴에 따른 뜻 힌트가 포함됩니다. `뜻 힌트:`로 시작하는 항목은 최종 사전 번역이 아니라 원문 정의를 바탕으로 한 임시 학습 힌트이므로 검토가 필요합니다.
- 모든 단어 카드에는 의미 키워드에 따라 숲속/생활 오브젝트 이모지 일러스트가 표시됩니다. 개별 손그림 721장은 포함하지 않습니다.


단어 카드의 시각 요소는 별도 그림 파일 없이 이모지 아이콘만 사용합니다. 한국어 뜻은 각 단어의 영어 정의를 기준으로 정리한 `words.json`의 `meaning_ko`를 표시합니다.
