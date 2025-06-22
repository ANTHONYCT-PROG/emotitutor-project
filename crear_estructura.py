import os

# Carpetas a crear
folders = [
    "backend/app/api/routes",
    "backend/app/core",
    "backend/app/models",
    "backend/app/services",
    "backend/app/db",
    "backend/app/schemas",
    "backend/app/utils",
    "backend/tests",
    "frontend/src/components/Chat",
    "frontend/src/components/Analysis",
    "frontend/src/components/TutorPanel",
    "frontend/src/components/Auth",
    "frontend/src/pages",
    "frontend/src/services",
    "frontend/src/store",
    "frontend/src/hooks",
    "frontend/src/styles",
    "frontend/src/utils",
    "ml_models/emotion_detection",
    "ml_models/style_classification",
    "docs"
]

# Archivos vacíos a crear
files = [
    "backend/app/main.py",
    "backend/app/api/routes/chat.py",
    "backend/app/api/routes/analysis.py",
    "backend/app/core/config.py",
    "backend/app/core/security.py",
    "backend/app/models/emotion.py",
    "backend/app/models/style.py",
    "backend/app/services/chat_service.py",
    "backend/app/services/analysis_service.py",
    "backend/app/db/session.py",
    "backend/app/db/models.py",
    "backend/app/db/crud.py",
    "backend/app/schemas/chat.py",
    "backend/app/schemas/analysis.py",
    "backend/app/utils/logger.py",
    "backend/app/utils/exceptions.py",
    "backend/app/dependencies.py",
    "backend/tests/test_chat.py",
    "backend/tests/test_analysis.py",
    "backend/Dockerfile",
    "backend/requirements.txt",
    "backend/README.md",
    "frontend/package.json",
    "frontend/src/components/Chat/ChatWindow.tsx",
    "frontend/src/components/Chat/MessageBubble.tsx",
    "frontend/src/components/Analysis/AnalysisPanel.tsx",
    "frontend/src/components/TutorPanel/AlertList.tsx",
    "frontend/src/components/TutorPanel/ChatDirect.tsx",
    "frontend/src/components/Auth/Login.tsx",
    "frontend/src/components/Auth/Register.tsx",
    "frontend/src/pages/chat.tsx",
    "frontend/src/pages/analysis.tsx",
    "frontend/src/pages/tutor.tsx",
    "frontend/src/pages/profile.tsx",
    "frontend/src/pages/settings.tsx",
    "frontend/src/services/api.ts",
    "frontend/src/services/auth.ts",
    "frontend/src/store/userSlice.ts",
    "frontend/src/store/chatSlice.ts",
    "frontend/src/hooks/useAuth.ts",
    "frontend/src/hooks/useChat.ts",
    "frontend/src/styles/globals.css",
    "frontend/src/utils/helpers.ts",
    "frontend/tsconfig.json",
    "frontend/tailwind.config.js",
    "frontend/next.config.js",
    "frontend/README.md",
    "ml_models/emotion_detection/train.py",
    "ml_models/emotion_detection/utils.py",
    "ml_models/emotion_detection/model.h5",
    "ml_models/style_classification/train.py",
    "ml_models/style_classification/utils.py",
    "ml_models/style_classification/model.joblib",
    "docker-compose.yml",
    ".env.example",
    "README.md",
    "docs/architecture.md",
    "docs/api_spec.md",
    "docs/user_guide.md"
]

# Crear carpetas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Crear archivos vacíos
for file in files:
    with open(file, "w") as f:
        pass

print("✅ Estructura del proyecto creada con éxito.")
