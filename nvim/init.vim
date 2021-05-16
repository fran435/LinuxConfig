" ------General------ "

syntax on
set termguicolors 
set scroll=5
set mouse=a
set noerrorbells
set number relativenumber
set clipboard+=unnamedplus
set numberwidth=1
set nowrap
set noswapfile
set nobackup
set ignorecase
set encoding=utf-8
set nocursorline
set nocursorcolumn
set termguicolors

highlight ColoColumn ctermbg=0 guibg=lightgrey

" ------Taburador------ "

set shiftwidth=4
set tabstop=4
set expandtab
set autoindent
filetype indent on

" ------Teclas------ "

let mapleader = ","

nnoremap <F1> :w<Enter>
nnoremap <F2> :q<Enter>
nnoremap <F3> :setlocal spell! spelllang=es<Enter>
nnoremap <F4> !!$SHELL<Enter>
inoremap ¿ ¿?<Esc>i
inoremap ¡ ¡!<Esc>i
inoremap [ []<Esc>i
inoremap ( ()<Esc>i
inoremap { {}<Esc>i
inoremap < <><Esc>i
inoremap " ""<Esc>i
inoremap ' ''<Esc>i
inoremap /* /**/<Esc>hi

" ------Plugins------ "

call plug#begin('~/.config/nvim/plugins')

Plug 'rbgrouleff/bclose.vim'
Plug 'francoiscabrol/ranger.vim'
Plug 'yggdroot/indentline'
Plug 'vim-airline/vim-airline-themes'
Plug 'vim-airline/vim-airline'
Plug 'luochen1990/rainbow'
Plug 'josegamez82/starrynight'
Plug 'sainnhe/everforest'
Plug 'tribela/vim-transparent'
Plug 'ap/vim-buftabline'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'mhinz/vim-startify'
Plug 'ryanoasis/vim-devicons'
Plug 'Jorengarenar/vim-MvVis'

call plug#end()

" ------Configuracion de Plugins------ "

let g:rainbow_active = 1
colorscheme everforest

"indentLine
let g:indentLine_color_term = 239
let g:indentLine_char_list = ['▏', '¦', '┆', '┊']
let g:indentLine_fileTypeExclude = ['startify']

" startify
let g:startify_padding_left = 10
let g:startify_session_persistence = 1
let g:startify_enable_special = 0
let g:startify_change_to_vcs_root = 1
let g:startify_lists = [
    \ { 'type': 'dir'       },
    \ { 'type': 'files'     },
    \ { 'type': 'sessions'  },
    \ { 'type': 'bookmarks' },
    \ { 'type': 'commands' },
    \ ]

let  g:startify_bookmarks =  [
    \ {'c': '~/.config/nvim'}
    \ ]

let g:startify_commands = [
    \ {'ch':  ['Health Check', ':checkhealth']},
    \ {'ps': ['Plugins status', ':PlugStatus']},
    \ {'pu': ['Update vim plugins',':PlugUpdate | PlugUpgrade']},
    \ {'uc': ['Update coc Plugins', ':CocUpdate']},
    \ {'h':  ['Help', ':help']},
    \ ]

let g:startify_custom_header = [
 \ '',
 \ '                                                         .-.                 ',
 \ '                 ___ .-.     .--.     .-.    ___  ___  (___)  ___ .-. .-.   ',
 \ '                (   )   \   /    \   /   \  (   )(   ) (   ) (   )   `   \  ',
 \ '                 |  .-. .  |  .-. | | .-. |  | |  | |   | |   |  .-.  .-. | ',
 \ '                 | |  | |  |  | | | | | | |  | |  | |   | |   | |  | |  | | ',
 \ '                 | |  | |  |  |/  | | | | |  | |  | |   | |   | |  | |  | | ',
 \ '                 | |  | |  |  | _.´ | | | |  | |  | |   | |   | |  | |  | | ',
 \ '                 | |  | |  |  .´.-. | | | |  \ \  / /   | |   | |  | |  | | ',
 \ '                 | |  | |  \  `-  / | `-´ |   \ `´ /    | |   | |  | |  | | ',
 \ '                (___)(___)  `.__.´   \._./     \__/    (___) (___)(___)(___)',
 \ '',
 \ '',
 \ ''
 \ ]

"coc
let loaded_netrw = 0
let g:omni_sql_no_default_maps = 1
let g:loaded_python_provider = 0
let g:loaded_perl_provider = 0
let g:loaded_ruby_provider = 0
let g:python3_host_prog = expand('/usr/bin/python3')

let g:coc_disable_startup_warning = 1
set hidden
set nobackup
set nowritebackup
set cmdheight=1
set updatetime=300
set shortmess+=c
set signcolumn=yes

let g:coc_snippet_next = '<Tab>'
let g:coc_snippet_prev = '<S-Tab>'

let g:coc_global_extensions = [
            \'coc-yank',
            \'coc-pairs',
            \'coc-json',
            \'coc-css',
            \'coc-html',
            \'coc-tsserver',
            \'coc-yaml',
            \'coc-lists',
            \'coc-snippets',
            \'coc-pyright',
            \'coc-clangd',
            \'coc-prettier',
            \'coc-xml',
            \'coc-syntax',
            \'coc-git',
            \'coc-marketplace',
            \'coc-highlight',
            \'coc-flutter',
            \'coc-java'
            \]

hi CocCursorRange guibg=#b16286 guifg=#ebdbb2

"airline
let g:airline_theme='deus'
let g:airline_skip_empty_sections = 1
let g:airline_section_warning = ''
let g:airline_section_x=''
let g:airline_section_z = airline#section#create(['%3p%% ', 'linenr', ':%c'])
let g:airline#parts#ffenc#skip_expected_string='utf-8[unix]'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_min_count = 2   " show tabline only if there is more than 1 buffer
let g:airline#extensions#tabline#fnamemod = ':t'        " show only file name on tabs
let airline#extensions#coc#error_symbol = '✘:'
let airline#extensions#coc#warning_symbol = '⚠:'
if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif
let g:airline_right_sep = ''
let g:airline_left_sep = ''
let g:airline_symbols.linenr = ''
let g:airline_symbols.branch = '⎇ '
let g:airline_symbols.dirty= ''
let g:airline_section_warning = ''
let g:airline_section_x=''
let g:airline_section_z = airline#section#create(['%3p%% ', 'linenr', ':%c'])
let g:airline#parts#ffenc#skip_expected_string='utf-8[unix]'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_min_count = 2   " show tabline only if there is more than 1 buffer
let g:airline#extensions#tabline#fnamemod = ':t'        " show only file name on tabs
let airline#extensions#coc#error_symbol = '✘:'
let airline#extensions#coc#warning_symbol = '⚠:'
if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif
let g:airline_symbols.linenr = ''
let g:airline_symbols.branch = '⎇ '
let g:airline_symbols.dirty= ''

