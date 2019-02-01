BUCKET := tempbucket345tgdg

do: noop


noop:
	@echo "I did nothing"

create_bucket:
	aws cloudformation validate-template --template-body file://deploy/static_site.yml
	aws cloudformation deploy \
		--template-file deploy/static_site.yml \
		--stack-name first-web-app-static-site \
		--parameter-overrides WebAppBucketName=$(BUCKET) \
		--tags semester=2018-fall project=first-web-app \
		--profile umncloud

sync_website:
	aws s3 sync static-site s3://$(BUCKET) --profile umncloud
