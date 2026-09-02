<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import LoadingState from './LoadingState.vue'

const props = defineProps({ source: { type: String, required: true } })
const diagram = ref('')
const loading = ref(true)
const error = ref('')
const shell = ref(null)
const viewport = ref(null)
const scale = ref(1)
const translateX = ref(0)
const translateY = ref(0)
const isDragging = ref(false)
let renderSequence = 0
let activePointerId = null
let pointerX = 0
let pointerY = 0

const MIN_SCALE = 0.5
const MAX_SCALE = 3
const SCALE_STEP = 0.2

const diagramTransform = computed(() =>
  `translate(${translateX.value}px, ${translateY.value}px) scale(${scale.value})`,
)
const zoomPercentage = computed(() => `${Math.round(scale.value * 100)}%`)

function clampScale(value) {
  return Math.min(MAX_SCALE, Math.max(MIN_SCALE, value))
}

function setScale(nextScale, originX, originY) {
  const clampedScale = clampScale(nextScale)
  const ratio = clampedScale / scale.value
  translateX.value = originX - (originX - translateX.value) * ratio
  translateY.value = originY - (originY - translateY.value) * ratio
  scale.value = clampedScale
}

function zoomBy(amount) {
  if (!viewport.value) return
  setScale(
    scale.value + amount,
    viewport.value.clientWidth / 2,
    viewport.value.clientHeight / 2,
  )
}

function handleWheel(event) {
  if (!viewport.value) return
  const bounds = viewport.value.getBoundingClientRect()
  setScale(
    scale.value + (event.deltaY < 0 ? SCALE_STEP : -SCALE_STEP),
    event.clientX - bounds.left,
    event.clientY - bounds.top,
  )
}

function resetView() {
  scale.value = 1
  translateX.value = 0
  translateY.value = 0
}

function startPan(event) {
  if (event.button !== 0) return
  activePointerId = event.pointerId
  pointerX = event.clientX
  pointerY = event.clientY
  isDragging.value = true
  viewport.value?.setPointerCapture(event.pointerId)
}

function movePan(event) {
  if (!isDragging.value || event.pointerId !== activePointerId) return
  translateX.value += event.clientX - pointerX
  translateY.value += event.clientY - pointerY
  pointerX = event.clientX
  pointerY = event.clientY
}

function endPan(event) {
  if (event.pointerId !== activePointerId) return
  if (viewport.value?.hasPointerCapture(event.pointerId)) {
    viewport.value.releasePointerCapture(event.pointerId)
  }
  activePointerId = null
  isDragging.value = false
}

async function enterFullscreen() {
  if (!document.fullscreenElement) {
    await shell.value?.requestFullscreen()
  } else {
    await document.exitFullscreen()
  }
}

async function renderDiagram() {
  loading.value = true
  error.value = ''
  try {
    const { default: mermaid } = await import('mermaid')
    mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: 'base', themeVariables: {
      primaryColor: '#dcebe5', primaryTextColor: '#123b2d', primaryBorderColor: '#025939', lineColor: '#167a58', secondaryColor: '#f8f5ed', tertiaryColor: '#ffffff', fontFamily: 'DM Sans, sans-serif',
    } })
    const id = `data-relationship-${++renderSequence}`
    const { svg } = await mermaid.render(id, props.source)
    diagram.value = svg
    resetView()
  } catch (renderError) {
    console.error('Failed to render Mermaid diagram', renderError)
    error.value = 'Diagram gagal dirender.'
  } finally {
    loading.value = false
  }
}

onMounted(renderDiagram)
watch(() => props.source, renderDiagram)
</script>

<template>
  <LoadingState v-if="loading" label="Rendering diagram…" compact />
  <div v-else-if="error" class="load-error"><p>{{ error }}</p></div>
  <div v-else ref="shell" class="diagram-shell">
    <div class="diagram-controls" aria-label="Diagram controls">
      <button type="button" title="Zoom out" aria-label="Zoom out" :disabled="scale <= MIN_SCALE" @click="zoomBy(-SCALE_STEP)">
        <font-awesome-icon icon="magnifying-glass-minus" />
      </button>
      <output aria-live="polite">{{ zoomPercentage }}</output>
      <button type="button" title="Zoom in" aria-label="Zoom in" :disabled="scale >= MAX_SCALE" @click="zoomBy(SCALE_STEP)">
        <font-awesome-icon icon="magnifying-glass-plus" />
      </button>
      <button type="button" title="Reset view" aria-label="Reset view" @click="resetView">
        <font-awesome-icon icon="rotate-left" />
      </button>
      <button type="button" title="Toggle fullscreen" aria-label="Toggle fullscreen" @click="enterFullscreen">
        <font-awesome-icon icon="expand" />
      </button>
    </div>
    <div
      ref="viewport"
      class="diagram-viewport"
      :class="{ 'is-dragging': isDragging }"
      @wheel.prevent="handleWheel"
      @pointerdown="startPan"
      @pointermove="movePan"
      @pointerup="endPan"
      @pointercancel="endPan"
    >
      <div
        class="mermaid-diagram"
        :class="{ 'is-dragging': isDragging }"
        :style="{ transform: diagramTransform }"
        v-html="diagram"
      ></div>
    </div>
  </div>
</template>
