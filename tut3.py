from ldap3 import Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL, MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE, OFFLINE_SLAPD_2_4
server = Server('my_fake_server', get_info=OFFLINE_SLAPD_2_4)
conn = Connection(server, 'uid=helpdesk,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'Secret123', auto_bind=False)
conn.bind()
print(1, conn.last_error)
print(conn.result)
conn.add('ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'organizationalUnit')
print(1, conn.last_error)
conn.add('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Beatrix', 'sn': 'Young', 'departmentNumber': 'DEV', 'telephoneNumber': 1111})
print(2, conn.last_error)
conn.modify_dn('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.smith')
print(3, conn.last_error)
conn.add('ou=moved, ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'organizationalUnit')
print(4, conn.last_error)
conn.modify_dn('cn=b.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.smith', new_superior='ou=moved, ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
print(5, conn.last_error)
conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_ADD, ['Smyth'])]})
print(6, conn.last_error)
conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_DELETE, ['Young'])]})
print(8, conn.last_error)
conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_REPLACE, ['Smith'])]})
print(9, conn.last_error)
conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_ADD, ['Young', 'Johnson']), (MODIFY_DELETE, ['Smith'])], 'givenname': [(MODIFY_REPLACE, ['Mary', 'Jane'])]})
print(10, conn.last_error)
conn.modify_dn('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.smith', new_superior='ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
print(11, conn.last_error)
conn.modify('cn=b.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_DELETE, ['Johnson'])], 'givenname': [(MODIFY_REPLACE, ['Beatrix'])]})
print(12, conn.last_error)
conn.modify_dn('cn=b.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.young')
print(13, conn.last_error)
conn.add('cn=m.johnson,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Mary Ann', 'sn': 'Johnson', 'departmentNumber': 'DEV', 'telephoneNumber': 2222})
print(14, conn.last_error)
conn.add('cn=q.gray,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Quentin', 'sn': 'Gray', 'departmentNumber': 'QA', 'telephoneNumber': 3333})
print(15, conn.last_error)

obj_person = ObjectDef('inetOrgPerson', conn)
r = Reader(conn, obj_person, '', 'ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
r.search()
print(r)
w = Writer.from_cursor(r)
print(w)
print(w[0])
e = w[0]
print(e.entry_dn)
print(e.entry_attributes)
print(e.entry_attributes_as_dict)
print(e.entry_mandatory_attributes)
print(e.entry_to_ldif())
print(e.entry_to_json(include_empty=False))
