.PHONY: env up

env = dev

## --- # Константы # --- #
# (не стоит их переопределять при вызове make)
compose = docker-compose.yml:docker-compose.${env}.yml
env_dir = conf/environments
base_env = $(env_dir)/.env.base
current_env = $(env_dir)/.env.$(env)
reverse_lines = sed '1!G;h;$$!d'
remove_duplicates = awk -F "=" '!a[$$1]++'


# Инициализация переменных окружения
# Записывает в .env содержимое файлов (в том же порядке):
#  - configs/environment/.env.base
#  - configs/environment/.env.{environment}
# Несуществующие файлы игнорируются
# Магия sed/awk удаляет дубликаты из .env, оставляя последнее значение
env:
	$(info ----- $@ start -----)
	@grep -v -h '^#' $(base_env) $(current_env) 2>/dev/null \
		| $(reverse_lines) | $(remove_duplicates) | sort > .env
	$(info ----- $@ done ----)

# Запуск/перезапуск проекта
up:
	@make -s env
	COMPOSE_FILE=$(compose) docker-compose pull
	COMPOSE_FILE=$(compose) docker-compose up --build -d
