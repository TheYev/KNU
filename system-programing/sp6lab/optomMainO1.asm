f(int):
        mov     eax, edi
        cmp     edi, 9999
        jle     .L7
        ret
.L7:
        sub     rsp, 8
        lea     edi, [rdi+1]
        call    f(int)
        add     rsp, 8
        ret
main:
        sub     rsp, 8
        mov     edi, 0
        call    f(int)
        mov     esi, eax
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(int)
        mov     eax, 0
        add     rsp, 8
        ret