from aiogram.utils.markdown import hide_link

# Add other languages and their corresponding codes as needed.
SUPPORTED_LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
}

TEXT_BUTTONS = {
    "ru": {
        "add": "﹢ Добавить",
        "back": "‹ Назад",
        "main": "≡ Главная",
        "retry": "↻ Повторить",
        "delete": "× Удалить",
        "confirm": "✓ Подтвердить",

        "connect_wallet": "Подключить {wallet_name}",
        "open_wallet": "Перейти в {wallet_name}",
        "disconnect_wallet": "× Отключиться",

        "change_language": "↻ Изменить язык",
        "get_access": "🔍 Проверить наличие доступа",

        "newsletter": "📰 Новостная рассылка",
        "admins_menu": "👥 Администраторы",
        "chats_menu": "💬 Чаты",
        "tokens_menu": "💎 Токены",
        "edit_min_amount": "✎ Изменить минимальную сумму",
    },
    "en": {
        "add": "﹢ Add",
        "back": "‹ Back",
        "main": "≡ Main",
        "retry": "↻ Retry",
        "delete": "× Delete",
        "confirm": "✓ Confirm",

        "connect_wallet": "Connect {wallet_name}",
        "open_wallet": "Go to {wallet_name}",
        "disconnect_wallet": "× Disconnect",

        "change_language": "↻ Change Language",
        "get_access": "🔍 Check access availability",

        "newsletter": "📰 Newsletter",
        "admins_menu": "👥 Admins",
        "chats_menu": "💬 Chats",
        "tokens_menu": "💎 Tokens",
        "edit_min_amount": "✎ Edit minimum amount",
    }
}

TEXT_MESSAGES = {
    "ru": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "🤖👋 <b>Приветствую</b>\n\n"
            "Я здесь, чтобы помочь тебе пройти верификацию и получить доступ в приватный клуб Брэда. "
            "Давай начнем 👌\n\n"
            "Клуб охраняется 🔒 и для доступа тебе необходимо хранить перечисленные токены. \n\n"
            
            "<b>Необходимые токены:</b>\n{tokens}\n\n"

            "<b>Подключен к:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://telegra.ph//file/6c433e5fdbdf439d63153.jpg')}"
            "👋 <b>Приветствую!</b>\n\n"
            "Выбери язык:"
        ),
        "change_language": (
            f"{hide_link('https://telegra.ph//file/6c433e5fdbdf439d63153.jpg')}"
            "<b>Выбери язык:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://telegra.ph//file/67c8d5f25c97ade6877eb.jpg')}"
            "🚫 <b>Вход запрещен</b>\n\n"
            "К сожалению, не обнаружены необходимые токены в твоем кошельке 😭.\n\n"
            "Не грусти, ты можешь <b>приобрести необходимые токены.</b> Перейди по кнопкам ниже и повтори попытку."
        ),
        "allow_access": (
            f"{hide_link('https://telegra.ph//file/67c8d5f25c97ade6877eb.jpg')}"
            " <b>Я знал 💪 </b>\n\n"
            "Ты 🫵 лучший и двери для тебя открыты\n\n"
            "<b>Жми на кнопку</b> ниже и входи в BRAD PRIVATE CLUB 😎 "
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Установить кошелек</a>\n\n"
            "<b>Подключи свой {wallet_name}!</b>\n\n"
            "Отсканируй с помощью мобильного кошелька:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Предупреждение</b>\n\n"
            "Подпись поддельна или время ожидания подключения истекло"
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Предупреждение</b>\n\n"
            "Время ожидания подключения истекло."
        ),

        "admin_menu": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Панель администратора</b>\n\nВыберите действие:"
        ),
        "chats_menu": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Меню приватных чатов</b>\n\nВыберите действие:"
        ),
        "chat_info": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "• <b>Информация о приватном чате</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>Тип:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>Название:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>Ссылка приглашения:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>Дата создания:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "<b>Меню токенов</b>\n\nВыберите действие:"
        ),
        "token_info": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "• <b>Информация о токене</b>\n\n"
            "• <b>Тип:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Название:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>Адрес:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>Минимальная сумма:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>Дата создания:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>Введите адрес токена</b>\n\nРазрешены только адреса коллекций NFT и мастеров Jetton:",
        "token_send_address_error": "Недопустимый адрес токена:\n{}",
        "token_send_address_error_already_exist": "Токен с адресом {address} уже существует!",
        "token_send_address_error_not_supported": "Контракт {interfaces} не поддерживается.\nПоддерживаются только {supported_interfaces}.",
        "token_send_amount": (
            "<b>Информация о токене</b>:\n\n"
            "• <b>Тип:</b>\n{token_type}\n"
            "• <b>Название:</b>\n{token_name}\n\n"
            "<b>Введите минимальную сумму токена</b> для доступа к приватному чату:"
        ),
        "token_edit_amount": "<b>Введите новую сумму токена</b> для доступа к приватному чату:",
        "token_send_amount_error": "Неверная сумма токена!",
        "admins_menu": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "<b>Меню администраторов</b>\n\nВыберите действие:"
        ),
        "admin_info": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "• <b>Информация об администраторе</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>Имя:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>Имя пользователя:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>Дата создания:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>Введите ID администратора:</b>",
        "admin_send_id_error": "Недопустимый ID:\n{}",
        "admin_send_id_error_not_found": "Администратор не найден. Сначала пользователь должен начать диалог с ботом.",
        "admin_send_id_error_not_member": "ID администратора должен быть числом.",
        "confirm_item_add": "<b>Подтвердите</b> добавление {item} в {table}?",
        "item_added": "{item} добавлен в {table}!",
        "confirm_item_delete": "<b>Подтвердите</b> удаление {item} из {table}?",
        "item_deleted": "{item} удален из {table}!"
    },
    "en": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "🤖👋 <b>Hi!</b>\n\n"
            "I'm here to help you get verified and gain access to Brad's private club. "
            "Let's get started 👌\n\n"
            "The club is guarded by 🔒 and you need to keep the listed tokens for access.\n\n"
            
            "<b>Required Tokens:</b>\n{tokens} \n\n"
            
            "<b>Connected to:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://telegra.ph//file/6c433e5fdbdf439d63153.jpg')}"
            "👋 <b>Hello!</b>\n\n"
            "Choose a language:"
        ),
        "change_language": (
            f"{hide_link('https://telegra.ph//file/6c433e5fdbdf439d63153.jpg')}"
            "<b>Choose a language:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://telegra.ph//file/67c8d5f25c97ade6877eb.jpg')}"
            "🚫 <b>Access Denied</b>\n\n"
            "Unfortunately, I did not detect the required tokens in your wallet 😭.\n\n"
            "Don't be sad, you can <b>purchase the necessary tokens.</b> Click on the buttons below and try again."
        ),
        "allow_access": (
            f"{hide_link('https://telegra.ph//file/67c8d5f25c97ade6877eb.jpg')}"
            " <b>I knew 💪</b>\n\n"
            "You are the best 🫵 and the doors are open for you\n\n"
            "<b>Click on the button below </b> and enter the BRAD PRIVATE CLUB 😎"
            
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Get a Wallet</a>\n\n"
            "<b>Connect your {wallet_name}!</b>\n\n"
            "Scan with your mobile app wallet:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Warning</b>\n\n"
            "The wallet signature is wrong or the connection timeout has expired."
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Warning</b>\n\n"
            "The connection timeout has expired."
        ),

        "admin_menu": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Administrator Panel</b>\n\nSelect action:"
        ),
        "chats_menu": (
            f"{hide_link('https://telegra.ph//file/34ad1113ee1b5683a9934.jpg')}"
            "<b>Private Chats Menu</b>\n\nSelect action:"
        ),
        "chat_info": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "• <b>Private Chat Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>Type:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>Invite Link:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "<b>Tokens Menu</b>\n\nSelect action:"
        ),
        "token_info": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "• <b>Token Information</b>\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>Address:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>Minimum Amount:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>Enter Token Address</b>\n\nOnly NFT collection and Jetton master addresses are allowed:",
        "token_send_address_error": "Invalid token address:\n{}",
        "token_send_address_error_already_exist": "Token with address {address} already exists!",
        "token_send_address_error_not_supported": "Contract {interfaces} is not supported.\nOnly {supported_interfaces} are supported.",
        "token_send_amount": (
            "<b>Token Information</b>:\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n\n"
            "<b>Enter the minimum token amount</b> to access the private chat:"
        ),
        "token_edit_amount": "<b>Enter the new token amount</b> to access the private chat:",
        "token_send_amount_error": "Invalid token amount!",
        "admins_menu": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "<b>Administrators Menu</b>\n\nSelect action:"
        ),
        "admin_info": (
            f"{hide_link('https://telegra.ph//file/fee8daf9a48db3d48f7b0.jpg')}"
            "• <b>Administrator Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>Username:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>Enter Administrator ID:</b>",
        "admin_send_id_error": "Invalid ID:\n{}",
        "admin_send_id_error_not_found": "Administrator not found. First, the user needs to start a conversation with the bot.",
        "admin_send_id_error_not_member": "Administrator ID must be a number.",
        "confirm_item_add": "<b>Confirm</b> adding {item} to {table}?",
        "item_added": "{item} added to {table}!",
        "confirm_item_delete": "<b>Confirm</b> deleting {item} from {table}?",
        "item_deleted": "{item} deleted from {table}!"
    }
}
