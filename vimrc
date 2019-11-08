# .vimrc
cat: /homes/cmishra/..vimrc: No such file or directory
[cmishra@evosb_oct24]$cat ~/.vimrc
":colorscheme evening
syntax on
set hlsearch
set backspace=indent,eol,start
set sw=4
set autoindent
filetype on
autocmd FileType c,cpp :set cindent!
set incsearch
set ruler
se ic
set shiftwidth=4
highlight Comment term=bold ctermfg=2
highlight String term=bold ctermfg=5 gui=bold
highlight Include ctermfg=3 guifg=bg
highlight Define cterm=bold ctermfg=3 guifg=bg
highlight Constant ctermfg=3 guifg=bg
:set expandtab
:set tabstop=4
:set shiftwidth=4
:set noautoindent
set listchars=trail:�
set listchars+=tab:�-
set listchars+=eol:�
:se tags=
:let s:ret = findfile("tags")
:let s:_wd = getcwd()
:if s:ret != "tags" && matchstr(s:_wd, "/9.2")
:se tags=~/t/tags.v92
:se notr
:cs add $WSPC/src/cscope.out $WSPC/src
:endif

:let s:ret = strlen($WSPC)
:if s:ret > 0 && empty(&tags)
:se tags=$WSPC/src/tags
:se tr
:endif

:let s:ret = findfile("cscope")
:if s:ret == "cscope"
:se cst
:cs add cscope
:endif

:nmap <C-\>s :cs find s <C-R>=expand("<cword>")<CR><CR>
:nmap <C-\>g :cs find g <C-R>=expand("<cword>")<CR><CR>
:nmap <C-\>c :cs find c <C-R>=expand("<cword>")<CR><CR>
:nmap <C-\>t :cs find t <C-R>=expand("<cword>")<CR><CR>
:nmap <C-\>e :cs find e <C-R>=expand("<cword>")<CR><CR>
:nmap <C-\>f :cs find f ^<C-R>=expand("<file>")<CR><CR>
:nmap <C-\>d :cs find d <C-R>=expand("<cword>")<CR><CR>

:nmap <C-;>s :scs find s <C-R>=expand("<cword>")<CR><CR>
:nmap <C-;>g :scs find g <C-R>=expand("<cword>")<CR><CR>
:nmap <C-;>c :scs find c <C-R>=expand("<cword>")<CR><CR>
:nmap <C-;>t :scs find t <C-R>=expand("<cword>")<CR><CR>
:nmap <C-;>e :scs find e <C-R>=expand("<cword>")<CR><CR>
:nmap <C-;>f :scs find f ^<C-R>=expand("<file>")<CR><CR>
:nmap <C-;>d :scs find d <C-R>=expand("<cword>")<CR><CR>

:nmap <C-[>s :vert scs find s <C-R>=expand("<cword>")<CR><CR>
:nmap <C-[>g :vert scs find g <C-R>=expand("<cword>")<CR><CR>
:nmap <C-[>c :vert scs find c <C-R>=expand("<cword>")<CR><CR>
:nmap <C-[>t :vert scs find t <C-R>=expand("<cword>")<CR><CR>
:nmap <C-[>e :vert scs find e <C-R>=expand("<cword>")<CR><CR>
:nmap <C-[>f :vert scs find f ^<C-R>=expand("<file>")<CR><CR>
:nmap <C-[>d :vert scs find d <C-R>=expand("<cword>")<CR><CR>

:set ignorecase
:set tags=tags;/
":set colorcolumn=80
