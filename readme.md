# main difference between my project and the TDD-Course

## Chapter 01

1. TDD-BOOK using python3.6 and Firefox, I using python3.7 and Chrome. So the there is not a geckodriver.log in my project.

## Chapter 09&10

1. TDD-BOOK use superlists-staging.ottg.eu, but in my project, I use staging.qicai21.cn instead. And I'm using this sitename in everywhere such as nginx config and foldpath.

## Chapter 12

- `wait_for_row_in_list_table` is in the book, but I'm using my `waiting_for`+`check_for_row_in_list_table` instead of that.

```python
# In the book
def wait_for_row_in_list_table(self, row_text):
	start_time = time.time()
	while True:
		try:
			table = self.browser.find_element_by_id('id_list_table')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn(row_text, [row.text for row in rows])
			return
		except (AssertionError, WebDriverException) as e:
			if time.time() - start_time > MAX_WAIT:
			raise e
			time.sleep(0.5)

```

