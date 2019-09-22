def is_palindrome(m_age,d_age):

	m_age=str(m_age)

	d_age=str(d_age)

	diff=len(m_age)-len(d_age)

	d_age=d_age.zfill(len(m_age))

	m_age=m_age[::-1}

	if m_age==d_age:

		return True

	else:

		return False
